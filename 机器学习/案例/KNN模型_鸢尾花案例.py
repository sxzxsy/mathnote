"""
回顾，机器学习项目的研发流程
    1.加载数据
    2.数据的预处理
    3.特征工程（特征提取，预处理,,,）
    4.模型训练
    5.模型评估
    6.模型预测
"""
# 1.导包
from sklearn.datasets import load_iris   # 加载鸢尾花测试集
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV # 分割训练集和测试集
from sklearn.preprocessing import StandardScaler  # 数据标准化的
from sklearn.neighbors import KNeighborsClassifier # KN算法，分类对象
from sklearn.metrics import accuracy_score # 模型评估的，计算模型预测的准确率

# 1.定义函数，加载鸢尾花数据集，并查看数据集
def dm01_loadiris():
    # 1.加载鸢尾花数据集
    iris_data  = load_iris()
    # # # 2.查看数据就
    # # print(f"数据集{iris_data}")
    # # print(f"数据集的类型{type(iris_data)}")
    # # # 3.查看数据及所有的键
    # print(f"数据集的所有键{iris_data.keys()}")
    # # 4.查看数据集所有的键对应的值
    # print(f"数据集的键对应的值{iris_data.data[:5]}")
    # # 5.查看数据集所有的键对应的标签值和名
    # print(f"数据集的键对应的标签值{iris_data.target[:5]}")
    # print(f"数据集的键对应的标签{iris_data.target_names[:5]}")
    # # 6.数据集的描述
    # print(f"数据集的描述{iris_data.DESCR}")
    # # 7.数据集的文件名
    # print(f"数据集的文件名{iris_data.filename}")
    # # 8.数据集的框架
    # print(f"数据集的框架{iris_data.frame}")

# 2.定义函数，绘制数据的散点图
def dm02_show_iris():
    # 1.加载数据
    iris_data = load_iris()
    # 把鸢尾花数据集封装成 Dataframe对象
    iris_df = pd.DataFrame(iris_data.data , columns=iris_data.feature_names)
    # 3.给df对象新增一列
    iris_df['lable'] = iris_data.target
    # 4.绘制数据
    sns.lmplot(data=iris_df,x='sepal length (cm)',y='petal length (cm)',hue='lable',fit_reg=False)
    # 参数一：数据集 ，参数二： x轴，参数三：y轴 参数四：hue 根据lable进行分类  参数五：fit_reg=False 绘制散点图，而不是曲线
    plt.title("iris_data")
    plt.show()

# 3.定义函数，切分训练集和测试集
def dm03_split_train_test():
    # 1.加载数据
    iris_data = load_iris ()
    # 2.数据的预处理：从150个特征和标签中，按照8:2的比例，切分训练集和测试集
    # 参数1：特征数据 参数2：标签数据 参数三：测试集的比例  参数4：随机种子（种子一致，每次生成的随机数据集都是固定的，这样不容易影响我们后期判断）
    # 返回值：训练集特征数据，测试集特征数据，训练集标签数据，测试集标签数据
    x_train,x_test,y_train,y_test = train_test_split(iris_data.data,iris_data.target,test_size=0.2,random_state=22)
    # 3.打印切分后的数据集
    print(f"训练集的特征：{x_train},个数：{len(x_train)}")  # 120条 每一条数据有4列（特征）
    print(f"训练集的标签：{y_train},个数：{len(y_train)}")   # 120条 每一条数据有1列（标签）
    print(f"测试集的特征：{x_test},个数：{len(x_test)}")   # 10条 每一条数据有4列（特征）
    print(f"测试集的标签：{y_test},个数：{len(y_test)}")   # 10条 每一条数据有1列（标签）
# 4. 定义函数，实现鸢尾花完整案例
"""
步骤：
    1.加载数据集
    2.数据预处理
    3.特征工程
    4.模型训练
    5.模型评估
    6.模型分析
"""
# 1. 加载数据集
def dm04_loadiris():
    # 1.加载数据集
    iris_data = load_iris()

    # 2.数据集预处理  将150条数据，按照训练集和测试集进行分割 比例8：2
    x_train,x_test,y_train,y_test = train_test_split(
        iris_data.data,iris_data.target,test_size=0.2,random_state=23)

    # 3.特征预处理 使用标注化进行特征预处理
       # 思考1.特征提取：因为原数据只有四个特征，且都是需要用的，所以我们这里不做特征提取
       # 思考2.特征预处理：因为源数据的4列特征值差值不大，所以这里不做特征预处理 但是，加入特征预处理，可以使我们的代码更完善
    # 3.1 创建标准化对象
    transfer = StandardScaler()
    # 3.2 对data特征列进行标准化操作  兼具fit和transform的功能，即：训练 ，转换 ，该函数适用于：第一次进行标准化的时候使用
    # 一般用于处理：训练集
    x_train= transfer.fit_transform(x_train)
    # transform:只有转换， 该函数适用于：重复进行标准化动作时使用，一般用于对测试集进行标准化
    x_test= transfer.transform(x_test)

    # 4.模型训练
    # 创建模型，便于求取最合适的n_neighbors个值
    estimator = KNeighborsClassifier()
    # 4.1定义字典，记录可能会出现的情况
    param_dict = {'n_neighbors': [i for i in range(1, 11)]}
    # 4.2 创建GridSearchCV对象 寻找最优超参 ，使用交叉验证+网络搜索
    # 参数一：estimator 模型对象
    # 参数二：超参数字典 该模型超参可能会出现的值
    # 参数三：交叉验证的次数 这里的次数指的是，每个超参组合，都会进行4次交叉验证 总计：10*4=40
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=4)
    # 4.3 模型训练 导入数据训练模型
    estimator.fit(x_train, y_train)
    # 4.4 打印最优超参组合
    print(f"最优超参组合：{estimator.best_params_}")  # {'n_neighbors': 3}
    print(f"最优评分：{estimator.best_score_}")


    # 4.1 创建模型
    estimator = KNeighborsClassifier(n_neighbors=3) # 通过交叉验证和网格搜索，找到最优超参组合为3
    # 4.2 训练模型
    estimator.fit(x_train,y_train)
    # 5.模型预测
    # 5.1 场景一：对刚才切分的测试集（30条）进行测试
    y_pre = estimator.predict(x_test)
    print(f"测试结果{y_pre}")
    # 5.2 场景二：对源数据之外的数据进行测试
    # 创建数据集
    my_data = [[7.8,2.1,8.5,2.2]]
    # 5.2.2 数据集标准化
    my_data = transfer.transform(my_data)
    # 5.2.3 模型预测
    y_pre_proba = estimator.predict_proba(my_data)
    print(f"预测结果为：{y_pre_proba}")

    # 6.模型评估
    # 6.1 方式1：直接评分，基于：测试集特征和测试集标签
    print(f"准确率：{estimator.score(x_test,y_test)}")
    # 6.2 方式2：基于：测试集标签和预测结果
    print(f"准确率：{accuracy_score(y_test,y_pre)}")




# 测试
if __name__ == '__main__':
    # dm01_loadiris()
    # dm02_show_iris()

    dm04_loadiris()