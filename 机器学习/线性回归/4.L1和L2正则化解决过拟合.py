"""
 案例：
    演示 欠拟合、正好拟合、过拟合 L1正则化  和L2正则化的  效果图

回顾：

    #欠拟合：在训练集和测试集上误差都较大的情况  模型过于简单
    #正好拟合：在训练集和测试集上误差都较小的情况
    #过拟合： 在训练集上误差较小，测试集误差较大的情况   模型过于复杂

过拟合、欠拟合解释：
    产生原因：
        欠拟合：模型简单
        过拟合：模型复杂
    解决方法：
        欠拟合：(1、添加其他特征项 2、添加多项式特征)
        过拟合：(1、重新清洗数据集 2、增大数据的训练量  3、正则化  4、减少特征维度)

什么叫正则化？
    在模型训练时，数据中有些特征影响模型复杂度、或者某个特征的异常值较多、所以要
    尽量减少这个特征的影响（甚至删除某个特征的影响），这就是正则化。
L1和L2正则化介绍：
    目的/思路：
        都是基于 惩罚系数 来修改（特征列的）权重的，惩罚系数越大，则修改力度越大，对应的权重越小
    区别：
        L1正则化，可以实现让权重变为0，从而达到特征选择的目的
        L2正则化，只能让权重无限接近于0，但是不能为0
"""
# 导包
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split   # 数据集划分
from sklearn.linear_model import LinearRegression      # 正规方程的回归模型
from sklearn.linear_model import SGDRegressor          # 梯度下降的回归模型
from sklearn.metrics import mean_squared_error, mean_absolute_error# 均方误差评估
from sklearn.linear_model import Ridge,RidgeCV,Lasso        #


# 1.定义函数，模拟：欠拟合
def under_fit():
    # 1.准备数据
    # 1.1指定随机种子，则每次生成（噪声）的数据都是固定的
    np.random.seed(23)
    # 1.2.随机生成x轴100个数据，模拟：特征
    x = np.random.uniform(-3,3,100)  # 参数1：最小值  参数2：最大值  参数3：生成个数
    # 1.3基于x轴值，通过线性公式随机生成y轴 100个数据，模拟：标签
    # 线性公式：y= kx+b
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0,1,100) # 参数1：平均值 参数2：标准差 3：生成个数
    # 1.4 查看生成的 x轴数据和y轴数据
    # print(f"特征：{x[:5]}")  # [1,2,3,4,5]
    # print(f"标签：{y[:5]}")

    # 2.数据预处理  把x轴（特征）转成 多行1列的形式
    X = x.reshape(-1,1)
    # print(f"特征：{X[:5]}") # [[1],[2],[3],[4],[5]]

    # 3.特征工程，这里不做了，直接用100条数据，先训练，后预测

    # 4.模型训练
    # 4.1创建模型对象
    estimator = LinearRegression()
    # 4.2模型训练
    estimator.fit(X,y)     # 参数1：处理后的特征数据 参数2：标签数据

    # 5.模型预测
    y_predict = estimator.predict(X) # 处理后的特征数据

    # 6.模型评估
    print(f"均方误差：{mean_squared_error(y,y_predict)}")

    # 7.绘图
    plt.scatter(x,y)   # 以散点图的形来绘制  真实值
    plt.plot(x,y_predict,color="red")  # 以线形图来绘制 预测值
    plt.show()


# 定义函数：正好拟合
def just_fit():
    # 1.准备数据
    # 1.1指定随机种子，则每次生成（噪声）的数据都是固定的
    np.random.seed(23)
    # 1.2.随机生成x轴100个数据，模拟：特征
    x = np.random.uniform(-3, 3, 100)  # 参数1：最小值  参数2：最大值  参数3：生成个数
    # 1.3基于x轴值，通过线性公式随机生成y轴 100个数据，模拟：标签
    # 线性公式：y= kx+b
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, 100)  # 参数1：平均值 参数2：标准差 3：生成个数
    # 1.4 查看生成的 x轴数据和y轴数据
    # print(f"特征：{x[:5]}")  # [1,2,3,4,5]
    # print(f"标签：{y[:5]}")

    # 2.数据预处理  把x轴（特征）转成 多行1列的形式
    X = x.reshape(-1, 1)
    # print(f"特征：{X[:5]}") # [[1],[2],[3],[4],[5]]
    # 2.1 因为目前特征列只有1列，模型过于简单，会出现欠拟合的问题，
    # 所以需要增加特征列，从而增加模型复杂度，从而避免欠拟合
    # 即：把数据从[[1],[2],[3],[4],[5]] ==> [[1,1],[2,4],[3,9],[4,16],[5,25]]
    X2 = np.hstack([X, X**2])
    print(f"特征：{X2[:5]}")

    # 3.特征工程，这里不做了，直接用100条数据，先训练，后预测

    # 4.模型训练
    # 4.1创建模型对象
    estimator = LinearRegression()
    # 4.2模型训练
    estimator.fit(X2, y)  # 参数1：处理后的特征数据 参数2：标签数据

    # 5.模型预测
    y_predict = estimator.predict(X2)  # 处理后的特征数据

    # 6.模型评估
    print(f"均方误差：{mean_squared_error(y, y_predict)}")

    # 7.绘图
    plt.scatter(x, y)  # 以散点图的形来绘制  真实值
    # np.sort(x) 对x进行排序 默认：升序
    # np.argsort(x) 对x进行排序，返回排序后的索引值
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color="red")  # 以线形图来绘制 预测值
    plt.show()

# 定义函数，模拟，过拟合
def over_fit():
    # 1.准备数据
    # 1.1指定随机种子，则每次生成（噪声）的数据都是固定的
    np.random.seed(23)
    # 1.2.随机生成x轴100个数据，模拟：特征
    x = np.random.uniform(-3, 3, 100)  # 参数1：最小值  参数2：最大值  参数3：生成个数
    # 1.3基于x轴值，通过线性公式随机生成y轴 100个数据，模拟：标签
    # 线性公式：y= kx+b
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, 100)  # 参数1：平均值 参数2：标准差 3：生成个数
    # 1.4 查看生成的 x轴数据和y轴数据
    # print(f"特征：{x[:5]}")  # [1,2,3,4,5]
    # print(f"标签：{y[:5]}")

    # 2.数据预处理  把x轴（特征）转成 多行1列的形式
    X = x.reshape(-1, 1)
    # print(f"特征：{X[:5]}") # [[1],[2],[3],[4],[5]]
    # 2.1 因为目前特征列只有1列，模型过于简单，会出现欠拟合的问题，
    # 为了模拟过拟合 所以需要增加特征列，从而增加模型复杂度
    # 即：把数据从[[1],[2],[3],[4],[5]] ==> [[1,1],[2,4],[3,9],[4,16],[5,25]]
    X3 = np.hstack([X, X ** 2, X ** 3,X ** 4, X ** 5, X ** 6, X ** 7, X ** 8, X ** 9, X ** 10])
    print(f"特征：{X3[:5]}")

    # 3.特征工程，这里不做了，直接用100条数据，先训练，后预测

    # 4.模型训练
    # 4.1创建模型对象
    estimator = LinearRegression()
    # 4.2模型训练
    estimator.fit(X3, y)  # 参数1：处理后的特征数据 参数2：标签数据

    # 5.模型预测
    y_predict = estimator.predict(X3)  # 处理后的特征数据

    # 6.模型评估
    print(f"均方误差：{mean_squared_error(y, y_predict)}")

    # 7.绘图
    plt.scatter(x, y)  # 以散点图的形来绘制  真实值
    # np.sort(x) 对x进行排序 默认：升序
    # np.argsort(x) 对x进行排序，返回排序后的索引值
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color="red")  # 以线形图来绘制 预测值
    plt.show()

# 定义函数 模型，L1正则化  Lasso回顾
def L1_Demo():
    # 1.准备数据
    # 1.1指定随机种子，则每次生成（噪声）的数据都是固定的
    np.random.seed(23)
    # 1.2.随机生成x轴100个数据，模拟：特征
    x = np.random.uniform(-3, 3, 100)  # 参数1：最小值  参数2：最大值  参数3：生成个数
    # 1.3基于x轴值，通过线性公式随机生成y轴 100个数据，模拟：标签
    # 线性公式：y= kx+b
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, 100)  # 参数1：平均值 参数2：标准差 3：生成个数
    # 1.4 查看生成的 x轴数据和y轴数据
    # print(f"特征：{x[:5]}")  # [1,2,3,4,5]
    # print(f"标签：{y[:5]}")

    # 2.数据预处理  把x轴（特征）转成 多行1列的形式
    X = x.reshape(-1, 1)
    # print(f"特征：{X[:5]}") # [[1],[2],[3],[4],[5]]
    # 2.1 因为目前特征列只有1列，模型过于简单，会出现欠拟合的问题，
    # 为了模拟过拟合 所以需要增加特征列，从而增加模型复杂度
    # 即：把数据从[[1],[2],[3],[4],[5]] ==> [[1,1],[2,4],[3,9],[4,16],[5,25]]
    X3 = np.hstack([X, X ** 2, X ** 3, X ** 4, X ** 5, X ** 6, X ** 7, X ** 8, X ** 9, X ** 10])
    print(f"特征：{X3[:5]}")

    # 3.特征工程，这里不做了，直接用100条数据，先训练，后预测

    # 4.模型训练
    # 4.1创建模型对象
    estimator = Lasso(alpha=0.1)  # alpha:正则化系数（惩罚系数），默认是1
    # 4.2模型训练
    estimator.fit(X3, y)  # 参数1：处理后的特征数据 参数2：标签数据

    # 5.模型预测
    y_predict = estimator.predict(X3)  # 处理后的特征数据

    # 6.模型评估
    print(f"均方误差：{mean_squared_error(y, y_predict)}")

    # 7.绘图
    plt.scatter(x, y)  # 以散点图的形来绘制  真实值
    # np.sort(x) 对x进行排序 默认：升序
    # np.argsort(x) 对x进行排序，返回排序后的索引值
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color="red")  # 以线形图来绘制 预测值
    plt.show()

# 定义函数 模拟 L2正则化  岭回归
def L2_Demo():
    # 1.准备数据
    # 1.1指定随机种子，则每次生成（噪声）的数据都是固定的
    np.random.seed(23)
    # 1.2.随机生成x轴100个数据，模拟：特征
    x = np.random.uniform(-3, 3, 100)  # 参数1：最小值  参数2：最大值  参数3：生成个数
    # 1.3基于x轴值，通过线性公式随机生成y轴 100个数据，模拟：标签
    # 线性公式：y= kx+b
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, 100)  # 参数1：平均值 参数2：标准差 3：生成个数
    # 1.4 查看生成的 x轴数据和y轴数据
    # print(f"特征：{x[:5]}")  # [1,2,3,4,5]
    # print(f"标签：{y[:5]}")

    # 2.数据预处理  把x轴（特征）转成 多行1列的形式
    X = x.reshape(-1, 1)
    # print(f"特征：{X[:5]}") # [[1],[2],[3],[4],[5]]
    # 2.1 因为目前特征列只有1列，模型过于简单，会出现欠拟合的问题，
    # 为了模拟过拟合 所以需要增加特征列，从而增加模型复杂度
    # 即：把数据从[[1],[2],[3],[4],[5]] ==> [[1,1],[2,4],[3,9],[4,16],[5,25]]
    X3 = np.hstack([X, X ** 2, X ** 3, X ** 4, X ** 5, X ** 6, X ** 7, X ** 8, X ** 9, X ** 10])
    print(f"特征：{X3[:5]}")

    # 3.特征工程，这里不做了，直接用100条数据，先训练，后预测

    # 4.模型训练
    # 4.1创建模型对象
    estimator = Ridge(alpha=0.1)
    # 4.2模型训练
    estimator.fit(X3, y)  # 参数1：处理后的特征数据 参数2：标签数据

    # 5.模型预测
    y_predict = estimator.predict(X3)  # 处理后的特征数据

    # 6.模型评估
    print(f"均方误差：{mean_squared_error(y, y_predict)}")

    # 7.绘图
    plt.scatter(x, y)  # 以散点图的形来绘制  真实值
    # np.sort(x) 对x进行排序 默认：升序
    # np.argsort(x) 对x进行排序，返回排序后的索引值
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color="red")  # 以线形图来绘制 预测值
    plt.show()

# 测试
if __name__ == '__main__':
    # under_fit() # 欠拟合
    # just_fit() # 正好拟合
    # over_fit() # 过拟合
    # L1_Demo() # L1
    L2_Demo()  #L2