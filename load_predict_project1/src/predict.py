# 导包
import os
import pandas as pd
import numpy as np
import datetime
from utils.log import Logger  # 日志
from utils.common import data_preprocseeing  # 导包函数调用
from xgboost import XGBRegressor  #XGboost
from sklearn.model_selection import train_test_split  # 数据集划分
from sklearn.model_selection import GridSearchCV   # 调参
from sklearn.metrics import mean_squared_error,mean_absolute_error,root_mean_squared_error,mean_absolute_percentage_error  # 均方误差，平均绝对误差
import joblib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rcParams['font.family'] = 'SimHei'  # 中文
plt.rcParams['font.size'] = 15


# 模型预测 将数据导入训练好的模型进行预测
# 1.配置电力负荷预测类
class PowerLoadPredict(object):
    def __init__(self,file_path):

        # 配置日志记录
        logfile_name = 'predict' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.logger = Logger('../', logfile_name).get_logger()
        # 获取数据源
        self.data_source = data_preprocseeing(file_path)
        # 历史数据转为字典，key：时间  value:负荷 ，目的是为了避免频繁操作dataframe。
        # 提高效率，实际开发场景中可以使用redis进行缓存
        # 格式为 {'2015-07-31 00:00:00': 801.59}
        self.time_load_dict = self.data_source.set_index('time').power_load.to_dict()


# 2.预测数据解析特征，保持与模型训练时的特征列名一致
def pred_feature_extract(data_dict,time,logger):
    """
    预测数据解析特征，保持与模型训练时
    1.解析时间特征
    2.解释时间窗口特征
    3.解析作日同时刻特征

    """
    logger.info(f"============解析预测时间为：{time}所对应的特征=========")
    # 特征列清单
    feature_names = ['hour_00', 'hour_01', 'hour_02', 'hour_03', 'hour_04', 'hour_05', 'hour_06',
    'hour_07', 'hour_08', 'hour_09', 'hour_10', 'hour_11', 'hour_12', 'hour_13', 'hour_14', 'hour_15',
    'hour_16', 'hour_17', 'hour_18', 'hour_19', 'hour_20', 'hour_21', 'hour_22', 'hour_23','month_01',
    'month_02', 'month_03', 'month_04', 'month_05', 'month_06', 'month_07', 'month_08', 'month_09', 'month_10',
    'month_11', 'month_12', '前1小时', '前3小时', '前2小时', 'yesterday_load']

    # 1.解析时间特征，即：time字段（预测时间）所对应的那条数据样本
    # 1.1 截取要预测的time字段的小时信息
    pre_hour = time[11:13] # 例如‘2015-08-30 04：00：00’——>‘04’
    hour_list= []
    for i in range(24):
        if pre_hour ==feature_names[i][5:7]:
            hour_list.append(1)
        else:
            hour_list.append(0)

    # 1.2 截取要预测的time中的月份信息
    pre_month =time[5:7]
    month_list = []
    for i in range(24,36):
        if pre_month ==feature_names[i][6:8]:
            month_list.append(1)
        else:
            month_list.append(0)

    # 2.解析时间窗口的特征
    # 前一个小时的负荷
    last_1h_time = (pd.to_datetime(time) - pd.Timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S") # 前一个时间
    last_1h_load = data_dict.get(last_1h_time,500)# 获取前一个时间的负荷，没有的话用500填充

    # 前2个小时的负荷
    last_2h_time = (pd.to_datetime(time) - pd.Timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")  # 前一个时间
    last_2h_load = data_dict.get(last_2h_time, 500)  # 获取前一个时间的负荷，没有的话用500填充

    # 前3个小时的负荷
    last_3h_time = (pd.to_datetime(time) - pd.Timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S")  # 前一个时间
    last_3h_load = data_dict.get(last_3h_time, 500)  # 获取前一个时间的负荷，没有的话用500填充

    # 昨天同时刻的负荷
    yesterday_time = (pd.to_datetime(time)-pd.Timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    yesterday_load = data_dict.get(yesterday_time,500)


    # 拼接特征数据
    feature_data = hour_list + month_list +[last_1h_load,last_2h_load,last_3h_load,yesterday_load]
    # print(feature_data)

    # #转成df类型
    feature_data = pd.DataFrame([feature_data],columns=feature_names)
    return feature_data


# 3.    # 绘制折线图(预测时间——真实负荷折线图，预测时间——预测负荷折线图)，查看测试效果
def prediction_plot(data):
    """
    :return:
    """
    fig, axes = plt.subplots(1, 2, figsize=(40, 20), dpi=80)
    axes[0].plot(evaluate_df['预测时间'], evaluate_df['真实负荷'], c='r', alpha=0.5)
    axes[1].plot(evaluate_df['预测时间'], evaluate_df['预测负荷'], c='g', alpha=0.5)
    axes[0].set_title('预测时间——真实负荷折线图', c='r')  # 添加标题
    axes[1].set_title('预测时间——预测负荷折线图', c='g')
    axes[0].grid(linestyle='-')  # 添加网格
    axes[1].grid(linestyle='-')
    # 设置刻度问题，以及x轴标签值 旋转角度
    axes[0].xaxis.set_major_locator(ticker.MultipleLocator(base=50))
    axes[1].xaxis.set_major_locator(ticker.MultipleLocator(base=50))
    axes[0].set_xlabel('时间')  # 添加 x轴标签
    axes[0].set_ylabel('负荷')
    axes[1].set_xlabel('时间')
    axes[1].set_ylabel('负荷')
    # 旋转x轴标签刻度
    plt.xticks(rotation = 45)
    axes[0].legend(loc=0)  # 不用添加set
    axes[1].legend(loc=0)
    # 保存
    plt.savefig('../data/fig/真实负荷与预测负荷之间的关系图.png')
    plt.show()

# 测试
if __name__ == '__main__':
    # 创建电力负荷预测类对象
    pp = PowerLoadPredict('../data/test.csv')
    # print(pp.data_source)
    # print(pp.time_load_dict)
    # 模型创建
    estimator = joblib.load("../model/xgb_20260517.pkl")
    # 确定要预测的时间段（2015-08-01 00：00：00及以后的时间
    pre_times = pp.data_source['time'][pp.data_source['time']>= '2015-08-01 00:00:00']

    # 定义evaluate_list列表，用于保存预测结果，方便后续进行结果评价
    evaluate_list = []

    # 为了模拟实际场景的预测，把要预测的时间及以后的负荷都掩盖掉，因此新建一个数据字典，只保存预测时间以前的数据字典
    for pre_time in pre_times:
        print(f"正在预测{pre_time}时间的负荷")
        time_load_maksed = {k:v for k,v in pp.time_load_dict.items() if k < pre_time}
        # 预测负荷
        feature_df = pred_feature_extract(time_load_maksed, pre_time, pp.logger)
        # 利用加载的模型预测
        y_pred = estimator.predict(feature_df)
        print(f"预测值{y_pred}")

        #保存预测时间对应的真实值
        true_value = pp.time_load_dict.get(pre_time,500)
        # 结果保存到evaluate_list ，三个元素分别是预测时间、真实时间、预测负荷，方便后去解析预测结果评价
        evaluate_list.append([pre_time,true_value,y_pred[0]])

    # 循环结束后，evaluate——list转为Dataframe
    evaluate_df = pd.DataFrame(evaluate_list,columns=["预测时间","真实负荷","预测负荷"])

    # 计算预测结果和真实结果的MAE
    print(f"平均绝对误差：{mean_absolute_error(evaluate_df['真实负荷'],evaluate_df['预测负荷'])}")

    # 绘制折线图(预测时间——真实负荷折线图，预测时间——预测负荷折线图)，查看测试效果
    prediction_plot(evaluate_df) # 方法调用
    # 保存折线图


