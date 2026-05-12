""""""
"""
案例：
    演示Boosting思想之 GBDT（梯度提升树）处理 泰坦尼克号数据集
    
GBDT 梯度提升树解释：
    概述：
        通过拟合 负梯度来获取一个强学习器
    流程：
        1.采用所有目标值的均值，作为第一个弱学习器的预测值
        2.目标值 - 预测值 = 负梯度（残差），该（列）值作为 第2个弱学习器的 目标值
        3.针对于第1个弱学习器，依次计算每个分割点的 最小平方和，找到最佳分割点，至此：第一个弱学习器搭建完成
        4.把上述的分割点带入第2个弱学习器，计算它的预测值 = 以此分割点为界，目标值的均值，即为该部分数据的 预测值
        5.计算第2个弱学习器的负梯度，最佳分割点，至此：第二个弱学习器搭建完成
        6.依此类推，直至程序结束"""

# 导入包
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier  #决策树分类
from sklearn.ensemble import GradientBoostingClassifier  # 梯度提升树
from sklearn.metrics import classification_report  # 模型评估
from sklearn.model_selection import GridSearchCV  # 网格搜索

# 1. 加载数据
data = pd.read_csv('泰坦尼克号数据集.csv')
# 2.数据预处理
# 2.1 抽取特征和标签
X = data[['Pclass', 'Age', 'Sex']].copy()
Y = data['Survived'].copy()
# 2.2 处理缺失值
X['Age'] = X['Age'].fillna(X['Age'].mean(),inplace=True) # 填充年龄 均值
# 2.3 类型转换 one-hot编码
X = pd.get_dummies(X,columns=['Sex']) # one-hot编码
# 3. 训练集和测试集的切分
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=22)

# 4.特征工程 （暂时忽略）
# 5.模型训练
estimator = DecisionTreeClassifier()
# 5.1模型训练
estimator.fit(X_train,Y_train)
#5.2 模型预测
y_pre = estimator.predict(X_test)
print(f"单个决策树对象预测结果是：{y_pre}")
# 6.模型评估
print(f"单个决策树的评估报告{classification_report(Y_test,y_pre)}")
print(25*"-")



# 7.创建GBDT模型
estimator_1 = GradientBoostingClassifier()
# 7.1 模型训练
estimator_1.fit(X_train,Y_train)
# 7.2 模型预测
y_pre_1 = estimator_1.predict(X_test)
print(f"GBDT模型预测结果是：{y_pre_1}")
# 7.3 模型评估
print(f"GBDT模型评估报告：{classification_report(Y_test,y_pre_1)}")


# 针对于GBDT（梯度提升树）模型，进行参数调优
# 8. 定义模型可选参数
param_grid = {'n_estimators':[50,100,150,200],   # 弱学习器的数量
              'learning_rate':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],  # 学习率
              'max_depth':[1,2,3,4,5,6,7,8,9,10]}   # 树最大深度




#9.1 创建网格搜索对象
# 参数1：调用模型对象 参数2：参数可选范围 参数3：交叉验证次数
estimator_2 = GridSearchCV(estimator_1,param_grid,cv=3)
# 9.2 模型训练
estimator_2.fit(X_train,Y_train)
print(f"最佳参数是：{estimator_2.best_params_}")
# 10.模型预测
y_pre_2 = estimator_2.predict(X_test)
print(f"预测结果是：{y_pre_2}")
# 11.模型评估
print(f"网格搜索后的模型准确率：{estimator_2.best_score_}")
print(f"网格搜索后的模型参数：{estimator_2.best_params_}")
print(f"网格搜索后的模型：{estimator_2.best_estimator_}")