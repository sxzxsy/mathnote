# 模型流程
"""
 1. 加载数据
 2.数据预处理（将数据集进行8/2 或者7/3进行分割）
 3.特征工程
 4.模型训练
 5.模型评估
 6.模型预测

"""
from sklearn.datasets import load_iris   # 加载鸢尾花测试集
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV # 分割训练集和测试集
from sklearn.preprocessing import StandardScaler  # 数据标准化的
from sklearn.neighbors import KNeighborsClassifier # KN算法，分类对象
from sklearn.metrics import accuracy_score # 模型评估的，计算模型预测的准确率

# 创建函数进行封装
# 1. 加载数据
y_flower  = load_iris()

# 2. 数据集预处理 将数据按照比例分割 test_size ：按照1的比例中的多少分割
x_train,y_train ,x_test,y_test = train_test_split(y_flower.data,y_flower.target, random_state=22,test_size=0.2)

# 3.特征工程 （对数据的进行度量，标准化）
#创建标准化对象
transfer = StandardScaler()
#对数据进行标准化操作
x_train_new = transfer.fit_transform(x_train)
x_test_new = transfer.transform(x_test)

# 4.模型训练
# 创建模型
estimator = KNeighborsClassifier() #n_neighbors 就是k
# 4.1定义字典，记录可能会出现的情况
param_dict = {'n_neighbors':[i for i in range(1,11)]}
# 4.2 创建GridSearchCV对象 寻找最优超参 ，使用交叉验证+网络搜索
# 参数一：estimator 模型对象
# 参数二：超参数字典 该模型超参可能会出现的值
# 参数三：交叉验证的次数 这里的次数指的是，每个超参组合，都会进行4次交叉验证 总计：10*4=40
estimator = GridSearchCV(estimator,param_grid=param_dict,cv=4)
# 4.3 模型训练 导入数据训练模型
estimator.fit(x_train,y_train)
# 4.4 打印最优超参组合
print(f"最优超参组合：{estimator.best_params_}") # {'n_neighbors': 3}
print(f"最优评分：{estimator.best_score_}")

# 5.测验
# 5.1 获取最优超参的模型对象
estimator = KNeighborsClassifier(n_neighbors =3 )
# 5.2模型训练
estimator.fit(x_train,y_train)
# 5.3模型预测
y_per = estimator.predict(y_test)
# 5.4模型评估
print(f"分数为{estimator.score(y_test,y_per)}")



