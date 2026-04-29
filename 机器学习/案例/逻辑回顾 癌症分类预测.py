# 导包
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression    # 逻辑回归模型
from sklearn.model_selection import train_test_split   # 测试集训练集分割
from sklearn.preprocessing import StandardScaler       # 标准化
from sklearn.metrics import accuracy_score             # 模型评估





# 1、数据加载
data = pd.read_csv("E:/data/breast-cancer-wisconsin.csv")
print(data.describe())
print(data.info())   #查看数据集信息

# 2、数据预处理  处理异常值和空值 划分数据集和测试集
# 参数1：待处理的数据集   参数2：用来填充的数据集  参数3：是否替换原数据集
data.replace('?', np.nan, inplace=True) # 将数据中的？替换为NaN
# 缺失值处理
data.dropna(inplace=True,ignore_index= True) # 删除有NaN的行 忽略索引

# 3、特征工程（提取、预处理）
# 特征提取之 提取特征和标签
x = data.iloc[: ,1:-1]  # 特征 1:-1 表示从索引1开始，到索引-1结束
y = data.iloc[: ,-1]   # 标签
# 查看一下特征和标签
# print(x[:5])
# print(y[:5])
# 训练集和测试集划分
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=23)
# 创建标准化对象
transfer = StandardScaler() # 创建标准化对象
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4、创建模型
estimator = LogisticRegression() # 创建逻辑回归模型
# 模型训练
estimator.fit(x_train,y_train)

# 5、模型预测
y_pre = estimator.predict(x_test)
print(f"预测结果为：{y_pre}")

# 6、模型评估
print(f"预测前评估 正确率：{estimator.score(x_test,y_test)}")
print(f"预测后评估 正确率：{accuracy_score(y_test,y_pre)}")

# 思考：逻辑回归模型能用 准确率来评估吗？
# 答案：可以，但是结果不准确，因为逻辑回归主要用于二分类，即A类和B类，不能说97%的A类，3%的B类
# 所以要通过混淆矩阵来评测，即：精确率，召回率，F1值（F1-Score），ROC曲线，AUC值


