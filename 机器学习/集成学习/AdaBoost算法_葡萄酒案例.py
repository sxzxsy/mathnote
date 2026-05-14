""""""
"""
案例： 
    演示AdaBoost算法 之 葡萄酒案例
AdaBoost算法介绍：
    它属于Boosting思想，即，串行执行、每次使用全部样本，最后加权投票
    原理：
        1.使用全部样本，通过决策树模型(第一个弱分类器进行训练)，获取结果，
            思路：
                预测正确————>权重降低
                预测错误————>权重增加
        2.把第一个弱分类器的处理结果，交给第二个弱分类器进行训练 ，获取结果。
            思路：
                预测正确————>权重降低
                预测错误————>权重增加
        3.依此类推 ，串行执行，直至获得最终结果"""


# 导入包
import pandas as pd
from sklearn.model_selection import train_test_split  # 划分
from sklearn.preprocessing import LabelEncoder   #标签编码器
from sklearn.tree import DecisionTreeClassifier   # 决策树分类器
from sklearn.ensemble import AdaBoostClassifier  #AdaBoost分类器————>集成学习Boosting思想
from sklearn.metrics import accuracy_score # 模型评估————正确率


# 1. 加载数据
data = pd.read_csv('E:/data/wine0501.csv')
# print(data.head())
# print(data.info())
# print(data.describe())

# 2. 数据预处理
# 2.1 从 标签列（Class label）中，过滤掉 1类别，剩下2，3类别
data = data[data['Class label'] != 1]
# 2.2 获取特征列
x = data[['Alcohol','Hue']]    # 酒精度，色调
y = data[['Class label']]   # 标签列

# 2.3 通过标签编码器，对标签列进行编码 ，把标签列转换为数值列
le = LabelEncoder()   # 标签编码器
y = le.fit_transform(y)   # 标签列进行编码 把2，3转为 0，1
# 2.4 划分数据集
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=22)

# 3.特征工程 省略

# 4.模型训练
# 场景1 单一决策树——>充当弱分类器
# 4.1创建模型
estimator = DecisionTreeClassifier(max_depth=3)  # 创建决策树分类器
# 4.2 模型训练
estimator.fit(x_train,y_train)
# 4.3 模型预测
y_pre = estimator.predict(x_test)
print(f"单一决策树预测结果：{y_pre}")
# 4.4 模型评估
print(f"单一决策树准确率：{accuracy_score(y_test,y_pre)}") # 0.8


# 场景2 AdaBoost————>集成学习 CART数，200棵
"""AdaBoost可以提高模型准确率，当创建了其他模型时，紧接着创建AdaBoost模型，
    将其他模型作为弱分类器参数，进而进行后续的模型训练等操作，以此来提高准确率"""
# 4.1创建模型
# 参数1：弱分类器，参数2：弱分类器个数，参数3：学习率  参数4：SAMME 集成算法
estimator2 = AdaBoostClassifier(estimator=estimator,n_estimators=200,learning_rate=0.1,algorithm='SAMME')
# 4.2 模型训练
estimator2.fit(x_train,y_train)
# 4.3 模型预测
y_pre2 = estimator2.predict(x_test)
print(f"AdaBoost预测结果：{y_pre2}")
# 4.4 模型评估
print(f"AdaBoost准确率：{accuracy_score(y_test,y_pre2)}")
