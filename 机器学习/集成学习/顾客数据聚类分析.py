# 导包
import os
os.environ['OMP_NUM_THREADS'] = '4' #设置OMP程序，运行时的线程数，避免任务多并发执行报错
# 导包
from sklearn.cluster import KMeans   #聚类的API ,采用指定质心 来分卒
import matplotlib.pyplot as plt     # 绘图
from sklearn.datasets import make_blobs  #默认会按照高斯分布(正态分布)生成数据集,只需要指定 均值,标准差
from sklearn.metrics import calinski_harabasz_score, silhouette_score  # 评价指标,值越大,聚类效果越好
import pandas as pd


def demo_1():
    # 定义函数，找 聚类的 质心
    # 读取数据
    df = pd.read_csv('E:/data/customers.csv')
    # print(df.info()) # 查看数据信息
    # 定义sse_list ,sc_list记录：不同K值，评估效果
    sse_list = []  # 只考虑簇间，越小越好
    sc_list = []   # 考虑簇间，簇内 ，越大越好
    # 抽取特征：
    x = df.iloc[:,3:5] # [‘行’，‘列’]
    # 定义for训练，测试不同K值，评估效果
    for k in range(2,20):
        # 创建模型
        estimator = KMeans(n_clusters=k,max_iter=100,random_state=23,n_init=10)
        # 模型训练
        estimator.fit(x)
        # 模型预测
        y_pred = estimator.predict(x)
        # 分别把评分添加到对应的列表中
        sse_list.append(estimator.inertia_)
        sc_list.append(silhouette_score(x,y_pred))
    # 绘制图像
    plt.figure(figsize=(20,10),dpi=80)
    # 传入数据直接画
    plt.plot(range(2,20),sse_list,label = 'SSE')
    plt.show()

    plt.figure(figsize=(20,10),dpi=80)
    plt.plot(range(2,20),sc_list,label = 'SC')
    plt.show()

# 定义函数，训练模型 ，就像预测评估
def demo_2():
    # 读取数据
    df = pd.read_csv('E:/data/customers.csv')
    # 抽取特征：
    x = df.iloc[:, 3:5]  # [‘行’，‘列’]
    # 创建模型 k=5是上边代码预测出来的
    estimator = KMeans(n_clusters=5, max_iter=100, random_state=23, n_init=10)
    # 模型训练
    estimator.fit(x)
    # 模型预测
    y_pred = estimator.predict(x)
    print(y_pred)
    # 绘制5各簇 样本的——散点图
    # 绘制5个簇 样本的——质心
    # x.values[y_pred ==0,0] 的意思是：
    plt.scatter(x.values[y_pred ==0,0],x.values[y_pred==0,1],label = 'Standard') # 0号簇
    plt.scatter(x.values[y_pred ==1,0],x.values[y_pred==1,1]) # 1号簇
    plt.scatter(x.values[y_pred ==2,0],x.values[y_pred==2,1]) # 2号簇
    plt.scatter(x.values[y_pred ==3,0],x.values[y_pred==3,1]) # 3号簇
    plt.scatter(x.values[y_pred ==4,0],x.values[y_pred==4,1]) # 4号簇
    # 绘制5个簇 质心 ——散点图
    # 参数1：质心坐标
    plt.scatter(estimator.cluster_centers_[:,0],estimator.cluster_centers_[:,1])

    # 设置标题，x轴，y轴标签
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income(k$)')
    plt.ylabel('Spending Score(1-100)')
    # 图例
    plt.legend()
    plt.show()

# 测试
if __name__ =="__main__":
    # demo_1()
    demo_2()