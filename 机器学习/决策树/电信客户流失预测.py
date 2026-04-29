'''
案例：
    通过逻辑回归算法，针对于电信用户数据建模，进行流失预测分析

'''

# 导包
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression    # 逻辑回归模型
from sklearn.model_selection import train_test_split   # 测试集训练集分割
from sklearn.preprocessing import StandardScaler       # 标准化
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,classification_report   # 模型评估
# 准确率、精确率、召回率、F1值、分类评估报告
import matplotlib.pyplot as plt
import seaborn as sns






# 1、定义函数，演示：数据预处理
def dm01_data_preprocess():
    # 1.1数据加载
    data = pd.read_csv("E:/data/churn.csv")
    # print(data.describe())
    # print(data.info())
    # 1.2新增两列 ，列名：Gender_Male Gender_Female 满足Gender_Male =Male的值为YES , Gender_Female = Female的值为NO
    # 因为数据集中的Churn,gender列是字符串，所以需要进行 one-hot编码（热处理编码）
    data = pd.get_dummies(data,columns=['gender','Churn'])
    # print(data.info())
    # data['Gender_Male'] = data['gender'].where(data['gender'] == 'Male', 'YES')
    # data['Gender_Female'] = data['gender'].where(data['gender'] == 'Female', 'NO')
    # print(data[['gender']][:5])
    # print(data[['Gender_Male','Gender_Female']][:5])
    # 1.3 删除one-hot编码后的 冗余的列
    data.drop(columns=['Churn_No','gender_Male'],inplace=True)
    # print(data.info())
    # 1.4修改列名 ，将Churn_Yes改为flag ,充当标签列
    data.rename(columns={'Churn_Yes':'flag'},inplace=True)

# 2、定义函数，查看数据可视化
def dm02_data_visualize():
    # 2.1 读取数据
    data = pd.read_csv("E:/data/churn.csv")
    # 2.2 对数据中的object类型做one-hot编码
    data =pd.get_dummies(data,columns=['gender','Churn'])
    # 2.3 删除one-hot编码后的 冗余的列
    data.drop(columns=['Churn_No','gender_Male'],inplace=True)
    # 2.4 修改列名 ，将Churn_Yes改为flag ,充当标签列
    data.rename(columns={'Churn_Yes':'flag'},inplace=True)
    # 2.5 查看数据值的分布
    print(data.flag.value_counts())# False:5174  True:1869
    # 2.6 查看列名，以便于进行后需操作
    # ['Partner_att', 'Dependents_att', 'landline', 'internet_att',
    #        'internet_other', 'StreamingTV', 'StreamingMovies', 'Contract_Month',
    #        'Contract_1YR', 'PaymentBank', 'PaymentCreditcard', 'PaymentElectronic',
    #        'MonthlyCharges', 'TotalCharges', 'gender_Female', 'flag'],
    # print(data.columns)

    # 2.7 绘制数据可视化  绘制计数柱状图
    # 参数1：x轴的列名（月度会员）  参数2：数据集 参数3：hue表示分组，根据分组进行绘制，这里是：是否流失Flase-不流失 True-流失
    sns.countplot(x='Contract_Month',data=data,hue='flag')
    plt.show()
# 3、定义函数，进行逻辑回归模型训练，预测，评估
def dm03_logistic_regression():
    # 3.1 读取数据
    data = pd.read_csv("E:/data/churn.csv")
    # 3.2 对数据中的object类型做one-hot编码
    data =pd.get_dummies(data,columns=['gender','Churn'])
    # 3.3 删除one-hot编码后的 冗余的列
    data.drop(columns=['Churn_No','gender_Male'],inplace=True)
    # 3.4 修改列名 ，将Churn_Yes改为flag ,充当标签列
    data.rename(columns={'Churn_Yes':'flag'},inplace=True)
    # 3.5 提取特征和标签
    x = data[['Contract_Month','internet_other','PaymentElectronic']]
    y = data[['flag']]  # False - 不流失 True-流失
    # 3.6 划分数据集和测试集
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=23)
    # 3.7特征工程（例如特征提取，特征预处理——归一化，标准化）暂不处理

    # 3.8 创建模型
    estimator = LogisticRegression() # 创建逻辑回归模型
    # 3.9 模型训练
    estimator.fit(x_train,y_train)
    # 3.10 模型预测
    y_pre = estimator.predict(x_test)
    print(f"预测结果为：{y_pre}")
    # 3.11 模型评估
    print(f"准确率：{accuracy_score(y_test,y_pre)}")
    print(f"精确率：{precision_score(y_test,y_pre)}")
    print(f"召回率:{recall_score(y_test,y_pre)}")
    print(f"f1值：{f1_score(y_test,y_pre)}")
    print(f"分类评估报告：{classification_report(y_test,y_pre)}")
    # macro avg:宏平平均值 即：不考虑样本权重，直接求平均，适用于：数据均衡的情况
    # weighted avg:加权平均值 即：考虑样本权重，求平均，适用于：数据不均衡的情况

# 测试
if __name__ == '__main__':
    # dm01_data_preprocess()
    dm02_data_visualize()
    dm03_logistic_regression()
