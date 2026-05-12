"""案例：
    泰坦尼克号案例：演示cart分类回归决策树的 分类功能"""

# 导包
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

#1. 加载数据
data = pd.read_csv('泰坦尼克号数据集.csv')
print(data.head())
print(data.info())
print(data.describe())

# 2. 数据预处理
# 2.1 提取特征和标签
x = data[['pclass', 'age', 'sex']]
y = data['survived']
# 2.2 缺失值处理
x = x.copy()
x['Age'] = x['Age'].fillna(x['Age'].mean(),inplace= True)   # 填充年龄 均值

# 2.3 针对于Sex列，进行one-hot编码
x = pd.get_dummies(x,columns=['Sex'])  # one-hot编码的意思：创建新的列，将原来的列进行二值化
# 2.4 划分数据集和测试集
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=23)

# 3. 创建模型
# 参数1：评价标准，参数2：最大深度
estimator= DecisionTreeClassifier(criterion='entropy',max_depth=5)
estimator.fit(x_train,y_train)

# 4.模型预测
y_per = estimator.predict(x_test)
print('预测结果：\n',y_per)

# 5.模型评估
print(f"分类评估报告：{classification_report(y_test,y_per)}")

# 6. 绘制决策树
plt.figure(figsize=(10,10))  # 设置图片大小
# 参数1：模型对象，参数2：是否显示颜色 ,参数3：最大深度
plot_tree(estimator,filled=True,max_depth=10)
plt.savefig('泰坦尼克号决策树.png')
plt.show()


