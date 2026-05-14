# XGBoost极端梯度提升树 ，集成学习的王牌
# 构建模型的方法是  最小化训练数据的损失函数  训练的模型复杂度越高，容易过拟合
# 基于打分函数的结果，决定是否分支
""""""


# XGboost实对GBDT的改进，且在损失函数中加入了正则化项，正则化项用来降低模型的复杂度
"""
步骤：
1.在损失函数的基础上 + 正则化(控制每个弱学习器的复杂度，叶子节点树 和树输出结果)
2.基于泰勒展开二阶式进行转换，转成 祭祀函数(使用t-1个弱学习器构成的继承模型损失求解当前t个弱学习器的损失)
3.把问题从 样本角度 ——>叶节点角度 进行分析
4.得到最终结论，打分函数 ——>Gain值 = 拆分前的分 - (拆分后左子树的分 + 拆分后右子树的分)
打分函数公式：obj^(t) = -1/2 ∑(G²/(Hi + λ)) + βT
从损失函数、树的复杂度两个角度来衡量一棵树的优劣。 最终的损失函数越小，代表模型越好

1.在损失函数的基础上 + 正则化(控制每个弱学习器的复杂度，叶子节点树 和树输出结果)
2.基于泰勒展开二阶式进行转换，(使用t-1个弱学习器构成的继承模型损失求解当前t个弱学习器的损失)
3.角度转换：统一将样本的计算转换树的角度
4.判断一个数是否要进行分类
"""


"""
案例：
    通过XGBoost极限梯度提升树 完成红酒品质分类
    
回顾：
    XGBoost 极限梯度提升树
    概述：
        Extreme Gradient Boosting Tree ,底层采用 打分函数 决定是否分支
    原理：
        Gain值 = 分支前的打分 - (分支后左子树打分 + 复制后右子树打分)
        如果Gain值 > 0 ，考虑分支 ，反之不考虑"""
# 导入XGboost包
import pandas as pd
import joblib
import xgboost as xgb    # 极限梯度提升树对象
import numpy as np
from sklearn.model_selection import train_test_split   # 数据集划分
from sklearn.metrics import classification_report, accuracy_score  # 模型分类评估报告,准确率
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import StratifiedKFold # 分层K折交叉验证，类似于 网格搜索时 cv = 折树
from sklearn.model_selection import GridSearchCV  #网格搜搜交叉验证
from sklearn.utils import class_weight          # 计算样本权重


def redjiu():
    # 1.数据集加载
    data = pd.read_csv('E:/data/红酒品质分类.csv')
    # print(data.info()) #查看数据集，看其中是否有异常数据据
    # 抽取特征数据和标签数据
    x = data.iloc[:, :-1]  # df.iloc[行号 , 列索引]
    y = data.iloc[:,-1]-3 # 最后一列是标签 ，默认值是[3,8]——>[0,5]
    # 2.切分训练集和测试集
    # 参数1：特征数据 参数2：标签数据 参数3：测试集的比例 参数4：随机种子 参数5：参考数据集的标签分布
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=23,stratify=y)
    # 2.1把上边的 训练集特征和标签数据拼接到一起，测试集特征和标签数据拼接到一起，最后写入文件中
    pd.concat([x_train,y_train],axis=1).to_csv("E:/data/红酒_train.csv",index = False) # axis =1 按行拼接
    pd.concat([x_test,y_test],axis=1).to_csv("E:/data/红酒_test.csv",index = False)

def learn_redj():
    # 1.加载数据
    train_data = pd.read_csv("E:/data/红酒_train.csv")
    test_data = pd.read_csv("E:/data/红酒_test.csv")
    # 2. 提取 训练集和测试集的特征数据和标签数据
    x_train = train_data.iloc[:,:-1]
    y_train = train_data.iloc[:,-1]

    x_test = test_data.iloc[:,:-1]
    y_test = test_data.iloc[:,-1]

    # 3.创建模型对象
    estimator =  xgb.XGBClassifier(
        max_depth =5,   # 树的最大深度
        n_estimators= 100,   # 树的数量
        learning_rate=0.1,  # 学习率
        random_state = 23, # 随机种子
        objective='multi:softmax'  # 多分类问题，使用多分类模型
    )
    # 加入 平衡权重， 因为数据集 是样本不均衡的
    # 参数1：平衡权重  参数2：标签数据（即：参考标签数据分布，平衡权重）
    class_weight.compute_sample_weight('balanced',y_train)
    # 4.模型训练
    estimator.fit(x_train,y_train)
    # 5.模型预测
    y_pre = estimator.predict(x_test)
    print(f"预测结果是：{y_pre}")
    # 6.模型评估
    print(f"准确率：{estimator.score(x_test,y_test)}")
    # 7.保存模型
    # 运行成功的前提是先创建一个model文件在执行
    joblib.dump(estimator,'E:/data/红酒品质分类.pkl') # 后缀名也可以写.pth, 都是pickle文件格式
    print("模型保存成功")

# 定义函数，测试模型
def use_model():
    # 1.加载数据
    train_data = pd.read_csv("E:/data/红酒_train.csv")
    test_data = pd.read_csv("E:/data/红酒_test.csv")
    # 2. 提取 训练集和测试集的特征数据和标签数据
    x_train = train_data.iloc[:, :-1]
    y_train = train_data.iloc[:, -1]

    x_test = test_data.iloc[:, :-1]
    y_test = test_data.iloc[:, -1]

    # 3.加载模型
    estimator = joblib.load('E:/data/红酒品质分类.pkl')
    # 4.创建网格搜索+交叉验证
    # 4.1 定义变量 记录：参数组合
    param_dict = {'max_path':[2,3,5,7,9],'n_estimators':[30,50,100,150],'learning_rate':[0.2,0.3,1,1.3]}
    # 4.2 创建分层采样 对象
    # 参数1：折树  参数2：是否打乱数据  参数3：随机种子
    skf = StratifiedKFold(n_splits=5,shuffle=True,random_state=23)
    # 4.3 创建网格搜索+交叉验证（结合分层采样数据）对象
    gs_estimator = GridSearchCV(estimator,param_dict,cv=skf)
    # 5.模型训练
    gs_estimator.fit(x_train,y_train)
    # 6.模型预测
    y_pre = gs_estimator.predict(x_test)
    print(f"预测结果：{y_pre}")
    # 7.模型评估
    print(f"最优模型组合：{param_dict}")
    print(f"模型评估报告{classification_report()}")
    print(f"最优评分{gs_estimator.best_score_}")
    print(f"准确率：{accuracy_score(y_test,y_pre)}")


# 测试
if __name__ == '__main__':
    #redjiu()
    #learn_redj()
    use_model()