"""
分类问题特点：有监督（有特征、有标签（不连续））
KNN算法，分类问题思路如下：
   1.计算测试集和每个训练的样本之间的距离。
   2.基于距离进行升序排列
   3.找到最近的K个样本
   4.K个样本进行投票
   5.票数多的结果作为最终的预测结果
   代码实现思路：
   1.导包
   2.准备数据集（测试集和训练集）
   3.创建KNN分类模型对象
   4.模型训练
   5.模型预测
    """
# 1.导包
from sklearn.neighbors import KNeighborsClassifier

# 2.准备数据集（测试集和训练集）
# [[a],[b],...] 这是一列  [[1,2],[3,4],]这是多行多列 1,2为一行，3，4为一行
# train ：训练集
# test：测试集
x_train = [[0],[1],[2],[3]] # 训练集特征  将数据包裹是因为训练集特征是多列的，所以是一个二维数组
y_train = [0,0,1,1] # 训练集标签   不包裹是因为标签就是只有一列
x_test = [[5]]   # 测试特征

# 3.创建KNN分类模型对象  estimator 估计器也可以用mode来命名
# KNeighborsClassifier 评估器
# neighbors：最近邻的邻居数（给他赋值 的时候要看训练集中有多少组数据，不能欠拟合，也不能过拟合，
# 即neighbors不能太小（过拟合），也不能太大（欠拟合）。
estimator = KNeighborsClassifier(n_neighbors=2) # n_neighbors：最近邻的邻居数也就是K值

# 取距离x_test最近(取差值最小的)的neighbors个x_train值，
# 根据对应的y_train投票取值
# 4.模型训练 fit拟合  传入训练集的特征数据，训练集的标签数据
estimator.fit(x_train,y_train)

# 5.模型预测
# 传入：.predict()——>预测 测试集的特征数据，进行结果预测（测试集的标签，y_test）
y_pre = estimator.predict(x_test)

# 6.打印预测结果
print(f"测试结果{y_pre}") # 1