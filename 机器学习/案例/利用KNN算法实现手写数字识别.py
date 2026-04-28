# 机器学习建模流程
"""
 1.数据加载
 2.数据预处理（对数据按照8/2或者7/3的比例进行分割）
 3.特征工程（特征预处理标准化：1.创建标准化对象transfer = StandardScaler()
           2.数据接入进行标准化处理 x_train= transfer.fit_transform(x_train)）
 4.模型训练（1.创建模型 estimator = KNeighborsClassifier(n_neighbors=3)
            2.接入数据进行模型训练estimator.fit(x_train,y_train)）
 5.模型预测 y_per = estimator.predict(x_text)
 6.模型评估 print(f"准确率：{accuracy_score(y_test,y_pre)}")
"""
# 导包
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split # 分割训练集和测试集
from sklearn.preprocessing import StandardScaler  # 数据标准化
from sklearn.neighbors import KNeighborsClassifier # KN算法，分类对象
from sklearn.metrics import accuracy_score # 模型评估的，计算模型预测的准确率
import joblib # 保存模型


# 定义函数进行封装
def show_digit(idx):
    # 1. 记载数据
    df= pd.read_csv('E:/python-leran/pythonlearn/data/手写数字识别.csv')
    # print(digits_data.head()) # head 方法，查看数据集的前五行
     # 判断传入的索引是否越界
    if idx <0 or idx > len(df) -1 :
        print("索引值超出范围")
        return
        # 2.数据预处理
    x = df.iloc[:,1:]  # 获取特征数据
    y = df.iloc[:, 0]  # 获取标签数据
    #2.1查看用户传入的索引对应的图片是多少
    print(f"用户输入的索引对应的图片为：{y.iloc[idx]}")
    # 将784像素点转为28*28的图片
    img = x.iloc[idx].values.reshape(28,28)  # dataframe设置reshape 参数 语法df.reshape(行数，列数)
    # 具体的绘制灰度图的动作
    plt.imshow(img,cmap='gray')  # 绘制灰度图
    plt.axis('off')   # 不显示坐标轴
    plt.show()


def show1_digit():
        # 1. 记载数据
        df = pd.read_csv('E:/python-leran/pythonlearn/data/手写数字识别.csv')
        # print(digits_data.head()) # head 方法，查看数据集的前五行
        # 判断传入的索引是否越界
        # if idx < 0 or idx > len(df) - 1:
        #     print("索引值超出范围")
        #     return
        # 2.数据预处理
        x = df.iloc[ : , 1:]  # 获取特征数据
        y = df.iloc[:,0] # 获取标签数据
        # 对特征列（分割前）进行归一化
        x = x / 255  # x = (x-0)/(255-0)
        x= np.ascontiguousarray(x.values)  # 转换为numpy数组
        y = y.values  # 转换为numpy数组
        # 数据集切分 stratify=y的意思是：按照标签进行切分，保证训练集和测试集的标签分布一致
        x_train,x_test,y_train,y_test = train_test_split(x , y,test_size=0.2,stratify= y,random_state=25)

        # # 3.特征预处理（标准化）
        # transfer = StandardScaler()  # 创建一个数据标准化对象
        # # 对数据集进行标准化
        # x_train = transfer.fit_transform(x_train)
        # x_test = transfer.transform(x_test)

        # 4.模型训练(KNN分类)
        estimator = KNeighborsClassifier(n_neighbors=3)  # 创建一个KNN分类器
        estimator.fit(x_train,y_train)
        # 5.模型预测
        y_per = estimator.predict(x_test)
        print(f"预测结果为：{y_per}")
        # 6.模型评估
        print(f"准确率：{accuracy_score(y_test,y_per)}")

        # 7.保存模型
        # 参数1：模型对象  参数2：保存的模型文件名
        joblib.dump(estimator,'E:/python-leran/pythonlearn/model/手写数字识别.pkl')
        print("保存模型成功")

# 模型测验评估展示
def use_model():
    # 1.加载图片
    x = plt.imread('E:/python-leran/pythonlearn/data/demo.png')
    # 2.绘制图片
    # plt.imshow(x,cmap='gray') #cmap='gray' 意思是：图片显示为灰色
    # plt.axis('off') # 不显示坐标轴
    # plt.show()
    # 3.加载模型
    estimator = joblib.load('E:/python-leran/pythonlearn/model/手写数字识别.pkl')
    # 4.查看数据集转换
    print(x.shape) # (28, 28)
    print(x.reshape(1,784).shape)  # (1, 784)
    print(x.reshape(1,-1).shape)  #效果同上
    # 具体转换动作：
    x = x.reshape(1,-1) # 可能会预测失败

    # 5.预测
    y_pre = estimator.predict(x)
    print(y_pre)

# 测试
if __name__ == '__main__':
    #show1_digit()  # 输入索引 调用函数显示索引对应的图片
    #
    use_model()