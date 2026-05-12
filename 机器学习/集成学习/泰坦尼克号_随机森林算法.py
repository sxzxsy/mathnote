# Titanic案例分析
""""""
"""
演示集成学习之Bagging思想  随机森林算法代码

集成学习：
    概述：
        把多个弱学习器 组成一个强学习器的过程 ——>集成学习
    思想：
        Bagging思想：
            1.有放回的随机抽样
            2.平权投票
            3.可以并行执行


        Boosting思想：
            1.每次训练都会使用全部样本
            2.加权投票——>预测正确：权重降低  预测错误：权重增加
            3.只能串行执行

随机森林算法：
    1.每个弱学习器都是CART数（必须是二叉树）
    2.有放回的随机抽样，平权投票，并行执行
"""
# 导包
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split  # 切分训练集和测试集
from sklearn.tree import DecisionTreeClassifier  # 决策树
from sklearn.ensemble import RandomForestClassifier  # 随机森林算法（分类器）
from sklearn.model_selection import GridSearchCV  # 网格搜索

# 1. 加载数据
data = pd.read_csv('泰坦尼克号数据集.csv')
# 2. 数据预处理
# 2.1 抽取 特征 和 标签
X = data[['Pclass', 'Age', 'Sex']].copy() # 船舱等级，年龄，性别
y = data['Survived']
# 2.2 缺失值处理
x = X.copy()
X['Age'].fillna(X['Age'].mean(), inplace=True)
# 2.3 类型 转换 one-hot编码
# one-hot编码的意思：创建新的列，列名是one-hot编码后的列名
x = pd.get_dummies(x, columns=['Sex'])
# 3. 训练集和测试集的切分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)
# 4. 特征过程 （暂时忽略）
# 5. 模型训练 决策树
estimator = DecisionTreeClassifier(criterion='entropy')
estimator.fit(X_train, y_train)
# 6.模型预测
y_pre = estimator.predict(X_test)
print(f"预测结果是：{y_pre}")
print(f"真实结果是：{y_test}")
# 7. 模型评估
print(f"决策树模型的准确率为：{estimator.score(X_test, y_test)}")
print(25*"-")

# 随机森林算法——> 采用默认参数
estimator_1 = RandomForestClassifier(n_estimators=100, max_depth=None)
estimator_1.fit(X_train, y_train)
# 模型预测
y_pre = estimator_1.predict(X_test)
print(f"预测结果是：{y_pre}")
print(f"真实结果是：{y_test}")
# 模型评估
print(f"随机森林模型的准确率为：{estimator_1.score(X_test, y_test)}")
print(25*"-")

# 随机森林算法——> 网格搜索
# 创建 随机森林对象，演示：多个决策树（Bagging思想）效果
estimator_2 = RandomForestClassifier()
estimator_2.fit(X_train, y_train)  # 细节：记得先训练一次
# 参数准备
param_grid = {'max_depth': [5, 6, 7, 8], 'n_estimators': [50, 60, 70, 80, 90, 100]}
# 创建 网格搜索对象结合交叉验证
params = GridSearchCV(estimator_2, param_grid, cv=3)
# 模型训练
estimator_2.fit(X_train, y_train)
# 模型预测
y_pre = estimator_2.predict(X_test)
print(f"预测结果是：{y_pre}")
# 模型评估
print(f"网格搜索的准确率为：{estimator_2.score(X_test, y_test)}")
# 获取最佳参数
print(f"最佳参数是：{params.best_params_}")
