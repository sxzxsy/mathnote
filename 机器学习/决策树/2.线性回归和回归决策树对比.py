""""""
"""
案例：
    演示：线性回归和决策树回归
    
细节：
    CART分类回顾决策树，既可以做分类，也可以做回归，一般做：分类，
    做分类是采用  基尼值，做回归时采用 平方损失(类似于 最小二乘)
"""

# 导包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor  # 回归决策树
from sklearn.linear_model import LinearRegression  # 线性回归


# 1.加载数据
x_train = np.array(list(range(1,11))).reshape(-1,1)
y_train = np.array([5.56,5.7,5.91,6.4,6.8,7.05,8.9,8.7,9,9.05])

# 2.数据预处理


# 3.特征工程（特征预处理）

# 4.模型训练
# 4.1分别创建线性回归和决策树回归
eistmator_01 = LinearRegression()  # 线性回归
eistmator_02 = DecisionTreeRegressor(max_depth=1)   # 回归决策树，最大数深度为1
eistmator_03 = DecisionTreeRegressor(max_depth=2)   # 回归决策树，最大数深度为3

# 4.2 模型训练
eistmator_01.fit(x_train,y_train)
eistmator_02.fit(x_train,y_train)
eistmator_03.fit(x_train,y_train)

# 5.模型预测
# 5.1 准备测试集的 特征数据
x_test = np.arange(0,10,0.1).reshape(-1,1)

# 5.3 预测
y_pre = eistmator_01.predict(x_test)
y_pre_01 = eistmator_02.predict(x_test)
y_pre_02 = eistmator_03.predict(x_test)

# 6.模型评估
print()

# 7.绘图
# 7.1以真实值（训练集）绘制散点图.
plt.scatter(x_train,y_train ,c='gray')
# 7.2以预测值（线性回归，回归决策树）绘制 折线图
plt.plot(x_test,y_pre,c='red',label = 'liner regression')
plt.plot(x_test,y_pre_01,c='blue',label = 'max depth=1')
plt.plot(x_test,y_pre_02,c='green',label = 'max depth=2')
# 7.3 显示图例
plt.legend()
# 7.4 设置x轴，y轴，标签
plt.xlabel('data')
plt.ylabel('target')
plt.title('Decision')
plt.show()
