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

plt.rcParams['font.family'] = 'SimHei'  # 中文
plt.rcParams['font.size'] = 15

# 1.定义电力负荷模型类，配置日志，获取数据源
class PowerLoadModel:
    # 1.1初始化属性信息
    def __init__(self,file_path):
        # 1.2拼接日志名
        logfile_name = 'train'+datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # 1.3 创建日志对象 参数1：父目录 参数2：子目录
        self.logfile = Logger('/log', logfile_name).get_logger()
        # 测试写一条日志
        self.logfile.info('开始创建 电力负荷模型类的  对象了')
        # 1.4 获取数据源
        self.df_source = data_preprocseeing(file_path)


# 2.查看数据的整体分布情况
def ana_data(df):
    """
    1.查看数据整体情况
    2.查看符合的分布情况
    3.各个小时的平均负荷趋势，看一下符合在一天中的变化情况
    4.各个月的平均负荷趋势，看一下符合在一年中的变化情况
    5.工作日与周末的平均符合情况，看一下工作日的符合与周末的负荷是否有区别
    :param data:
    :return:
    """
    # 0.为了防止被修改原数据，我们做一次拷贝
    ana_data = df.copy()
    # 1.查看数据整体情况
    ana_data.info()
    # 2.查看总负荷的分布情况,直方图
    # 2.1创建画布
    fig = plt.figure(figsize=(20,40),dpi=80)
    # 2.2添加子图
    ax1 = fig.add_subplot(411)  # 411的意思是
    # 添加标题和x刻度
    ax1.set_title("整体负荷分布情况")
    ax1.set_xlabel('负荷')
    ax1.hist(ana_data['power_load'],bins=100)  # 负荷 直方图 100个区间

    # 3.各个小时的平均负荷趋势，看一下符合在一天中的变化情况
    # 3.1 新增一列，当作小时
    ana_data['hour'] = ana_data['time'].str[11:13]
    # 3.2根据小时分组，计算平均值
    load_hour_mean = ana_data.groupby('hour',as_index = False)['power_load'].mean()
    # 画折线图
    ax2 = fig.add_subplot(412)
    # 添加标题和x刻度
    ax2.set_title('每天各个时段负荷分布情况')
    ax2.set_xlabel('负荷')
    ax2.plot(load_hour_mean['hour'],load_hour_mean['power_load'])

    # 4.各个月的平均负荷趋势，看一下符合在一年中的变化情况
    # 4.1 新增一列，当作月份
    ana_data['month'] = ana_data['time'].str[5:7]
    # 4.2 根据月分组，计算负荷平均值
    load_month_mean = ana_data.groupby('month',as_index=False)['power_load'].mean()
    # 画图
    ax3 = fig.add_subplot(413)
    # 添加标题和x刻度
    ax3.set_title("每月负荷分布情况")
    ax3.set_xlabel('负荷')
    ax3.plot(load_month_mean['month'],load_month_mean['power_load'])

    # 5.工作日与周末的平均符合情况，看一下工作日的符合与周末的负荷是否有区别
    ana_data['week_day'] = ana_data['time'].apply(lambda x:pd.to_datetime(x).weekday())
    ana_data['is_holiday'] = ana_data['week_day'].apply((lambda x: 1 if x in[5,6] else 0)) # 1节假日 0 工作日
    work_week_mean = ana_data[ana_data['is_holiday']==0].power_load.mean() # 工作日的值
    load_week_mean = ana_data[ana_data['is_holiday'] ==1].power_load.mean() # 节假日值
    # 绘制
    ax4 = fig.add_subplot(414)
    ax4.set_title("工作日和节假日负荷分布情况")
    ax4.set_xlabel('负荷')
    ax4.bar(['工作日','周末'],[work_week_mean,load_week_mean])

    # 保存
    plt.savefig('../data/fig/整体负荷分布情况.png')
    plt.show()

# 3.特征工程(重点)
def feature_engineering(data,logger):  # 参数1：数据 参数2：日志

    """
       1.提取出时间特征：小时、月份
       2.提取出相近时间的窗口中的负荷特征：step大小窗口的负荷
       3.提取昨日同时刻负荷样本
       4.剔除出现空值的样本
       5.整理时间特征，并返回
       :param data:
       :return:
       """
    logger.info("-------------开始特征工程处理------------")
    # 先拷贝原数据，防止被修改
    feature_data = data.copy()
    logger.info("-------------开始提取时间特征------------")
    # 1.提取出时间特征：小时、月份
    feature_data['hour'] = feature_data['time'].str[11:13]
    feature_data['month'] = feature_data['time'].str[5:7]
    # 热编码one-hot 处理 'month'和‘hour’字段
    # 两个中括号的原因：是为了传入一个列表作为索引，进而从dataframe中筛选出多列，返回一个新的dataframe
    hour_month_data = pd.get_dummies(feature_data[['hour','month']])
    # 拼接hour_month_data和feature_data
    feature_data = pd.concat([feature_data,hour_month_data],axis=1)  # 按行合并
    # print(feature_data.head(10))

    # 2.提取出相近时间窗口中的负荷特征：step大小窗口的负荷
    load_1h_data = feature_data['power_load'].shift(1) # 前一个小时的Power
    load_2h_data = feature_data['power_load'].shift(2) # 前两个小时的power
    load_3h_data = feature_data['power_load'].shift(3)
    load_shift_df = pd.concat([load_1h_data,load_2h_data,load_3h_data],axis=1) # 拼接
    load_shift_df.columns = ['前1小时','前3小时','前2小时']
    # 总拼接 将获取的相近时间的负荷和小时，月份的负荷月总数据表进行拼接
    feature_data = pd.concat([feature_data,load_shift_df],axis=1)
    # print(feature_data.info())

    # 3.提取昨日同时刻负荷特征
    # 给特征新增1列名，yesterday_time
    feature_data['yesterday_time'] = feature_data['time'].apply(
        lambda x:(pd.to_datetime(x) - datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'))
    # 我们把所有的 key:日期和 value:负荷 拼接成字典dict，方便查找
    time_load_dict = feature_data.set_index('time')['power_load'].to_dict()
    # 新增一列 yesterday_load表示：昨天的相同时刻的负荷
    feature_data['yesterday_load'] = feature_data['yesterday_time'].apply(lambda x:time_load_dict.get(x))

    # 4.删除出现空值的样本
    feature_data = feature_data.dropna()

    # 5.整理时间特征，并返回
    feature_columns = list(hour_month_data.columns)+ list(load_shift_df.columns) +['yesterday_load']
    print(feature_columns) # ['hour_00', 'hour_01', 'hour_02', 'hour_03', 'hour_04', 'hour_05', 'hour_06',
    # 'hour_07', 'hour_08', 'hour_09', 'hour_10', 'hour_11', 'hour_12', 'hour_13', 'hour_14', 'hour_15',
    # 'hour_16', 'hour_17', 'hour_18', 'hour_19', 'hour_20', 'hour_21', 'hour_22', 'hour_23', 'month_01',
    # 'month_02', 'month_03', 'month_04', 'month_05', 'month_06', 'month_07', 'month_08', 'month_09', 'month_10',
    # 'month_11', 'month_12', '前1小时', '前3小时', '前2小时', 'yesterday_time'].
    # 返回结果
    return feature_data,feature_columns

# 4.模型训练，保存，评估
def model_train(data,features,logger):
    """
       1.查看数据整体情况
       2.查看符合的分布情况
       3.各个小时的平均负荷趋势，看一下符合在一天中的变化情况
       4.各个月的平均负荷趋势，看一下符合在一年中的变化情况
       5.工作日与周末的平均符合情况，看一下工作日的符合与周末的负荷是否有区别
       :param data: 特征工程处理后的数据输入
       :param features: 特征名称
       :param logger:日志对象
       :return:
       """
    # 1.数据集划分
    x = data[features]
    y = data['power_load']

    # 添加调试日志
    logger.info(f"特征数据形状: {x.shape}")
    logger.info(f"目标变量形状: {y.shape}")
    logger.info(f"特征列数量: {len(features)}")
    logger.info(f"特征列名: {features}")
    logger.info(f"x中是否存在空值: {x.isnull().any().any()}")
    logger.info(f"y中是否存在空值: {y.isnull().any().any()}")

    if len(x) == 0:
        logger.error("错误：特征数据为空！")
        raise ValueError("特征数据为空，无法进行训练")
    # 划分训练集，测试集，标签
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=23)


    # # 网格搜素和交叉验证 获取最优超参组合
    logger.info('--------网格搜索+交叉验证 寻找最优超参数------------')
    logger.info(f'开始时间：{datetime.datetime.now()}')
    # # 定义参数字典
    # param_dict = {
    #     'n_estimators':[50,100,150,200],
    #     'max_depth':[3,5,7,9],
    #     'learning_rate':[0.01,0.1]
    # }
    # # 创建xgboost 模型对象
    # estimator = XGBRegressor()
    # # 创建网格搜索对象 参数1：模型对象 参数2：参数组合 参数3：2折法
    # gs = GridSearchCV(estimator=estimator,param_grid=param_dict,cv=2)
    # # 模型训练
    # gs.fit(x_train,y_train)
    # # 打印最优参数组合 最优参数组合：{'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 150}
    # logger.info(f"最优参数组合：{gs.best_params_}")
    logger.info(f"结束时间：{datetime.datetime.now()}")

    logger.info("带入最优参数，创建xgboost模型")
    # 3.模型实例化 将获取的最优参数传入 创建XGBoost模型
    estimator = XGBRegressor(learning_rate=0.1,max_depth=5,n_estimators=150)
    # 模型训练
    estimator.fit(x_train,y_train)
    y_pred = estimator.predict(x_test)
    # 模型评价
    print(f"均方误差：{mean_squared_error(y_test,y_pred)}")
    print(f"均方根误差:{root_mean_squared_error(y_test,y_pred)}")
    print(f"平均绝对误差：{mean_absolute_error(y_test,y_pred)}")
    print(f"平均绝对百分比误差：{mean_absolute_percentage_error(y_test,y_pred)}")
    logger.info(f"模型训练完成，当前时间：{datetime.datetime.now()}")
    # 模型保存
    joblib.dump(estimator, '../model/xgb_20260517.pkl')
    logger.info("模型保存成功")
# 测试
if __name__ == '__main__':
    # 1.创建对象
    pm = PowerLoadModel('../data/train.csv')
    # # 2.查看数据源
    # # print(pm.df_source)
    # # 3.查看数据分布
    # # ana_data(pm.df_source)
    # # 4.特征工程
    feature_data,feature_columns = feature_engineering(pm.df_source,pm.logfile)
    # # 5.模型训练
    model_train(feature_data,feature_columns,pm.logfile)
