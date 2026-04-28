# 导包
from sklearn.preprocessing import StandardScaler       # 特征处理
from sklearn.model_selection import train_test_split   # 数据集划分
from sklearn.linear_model import LinearRegression      # 正规方程的回归模型
from sklearn.linear_model import SGDRegressor          # 梯度下降的回归模型
from sklearn.metrics import mean_squared_error, mean_absolute_error# 均方误差评估
from sklearn.linear_model import Ridge,RidgeCV         #

import pandas as pd
import numpy as np

# 加载数据    因为波士顿数据有问题，只能这样加载
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])  # 水平拼接数组 np.hstack()
target = raw_df.values[1::2, 2]

# 数据集预处理 划分数据集和测试集
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=22)

# 特征预处理
# 创建标准化对象
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)


def L_R():
    # ----------------------------------正规方程----------------------------------
    # 创建模型
    # 创建线性回归 "正规方程"  模型对象
    estimator = LinearRegression(fit_intercept= True)   # fit_intercept：是否需要计算截距 默认为True

    # 训练模型
    estimator.fit(x_train,y_train)
    # 打印：模型计算出的w（权重） 和 b（截距）
    print(f"w:{estimator.coef_}")
    print(f"b:{estimator.intercept_}")

    # 模型预测
    y_per = estimator.predict(x_test)
    print(f"预测结果为：{y_per}")

    # 模型评估
    print(f"均方误差为：{mean_squared_error(y_test,y_per)}")    # MSE: 均方误差 J(W,b) = (h(x^i) - y^i)²/ 样本总数
    print(f"均方根误差为：{np.sqrt(mean_squared_error(y_test,y_per,))}")  # RMSE: 均方根误差J = √MSE
    print(f"平均绝对误差：{mean_absolute_error(y_test,y_per)}")  # MAE: 平均绝对误差J(W,b) = |(h(x^i) - y^i)|/ 样本总数


def T_D():
# -----------------------------------梯度下降法-----------------------------------
    # 创建模型
    # 梯度下降
    estimator = SGDRegressor(fit_intercept= True,learning_rate='constant',eta0=0.01)
    # 参数1：是否计算截距 默认为True  截距是模型预测结果与真实结果之间的差距
    # 参数2：学习率 默认是constant，表示每次迭代时学习率不变
    # 参数3：每次迭代时学习率

    # 模型训练
    estimator.fit(x_train,y_train)
    # 打印：模型计算出的w（权重） 和 b（截距）
    print(f"w:{estimator.coef_}")
    print(f"b:{estimator.intercept_}")

    # 模型预测
    y_per = estimator.predict(x_test)
    print(f"预测结果为：{y_per}") 

    # 模型评估
    print(f"均方误差为：{mean_squared_error(y_test, y_per)}")  # MSE: 均方误差 J(W,b) = (h(x^i) - y^i)²/ 样本总数
    print(f"均方根误差为：{np.sqrt(mean_squared_error(y_test, y_per))}")  # RMSE: 均方根误差J = √MSE
    print(f"平均绝对误差：{mean_absolute_error(y_test, y_per)}")  # MAE: 平均绝对误差J(W,b) = |(h(x^i) - y^i)|/ 样本总数



# 测试
if __name__ == '__main__':
    # L_R() # 线性回归 正规方程法
    T_D() # 线性回归 梯度下降法
