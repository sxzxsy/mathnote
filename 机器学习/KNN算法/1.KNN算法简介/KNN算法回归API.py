"""
回归问题特点： 有监督(有特征，有标签且标签连续)
KNN算法回归问题步骤
    1.计算测试集和每个训练集样本之间的距离
    2.基于距离进行升序排序
    3.找到最近的K个样本
    4.对K个样本进行求均值
    5.将均值结果作为最终预测结果
代码实现思路：
   1.导包
   2.准备数据集（测试集和训练集）
   3.创建KNN回归模型对象
   4.模型训练
   5.模型预测
"""

# 1.导包
from sklearn.neighbors import KNeighborsRegressor

# 2.准备数据集
x_train = [[0,0,1],[1,1,0],[3,10,10],[4,11,12]]
y_train = [0.1,0.2,0.3,0.4]
x_test = [[3,11,10]]

# 3.创建KNN回归模型
estimate = KNeighborsRegressor(n_neighbors=2)

# 4.模型训练 传入数据
# 取距离x_test最近(取差值最小的)的neighbors个x_train值
# 根据其y_train的对应值进行求和取均值
estimate.fit(x_train,y_train)

# 5.模型预测
y_pre = estimate.predict(x_test)

# 6.预测结果
print(f"结果是{y_pre}") # 0.25