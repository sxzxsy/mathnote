""""""
""" 了解就行
聚类算法:   
       无监督学习算法,主要用于将相似的样本自动归到一个类别中;
       计算样本之间的相似性,一般通过欧氏距离
应用场景:例如抖音视频推送,会根据个人喜好,推送数据
聚类分类:
        颗粒度:粗聚类,细聚类
        实现方法:K-mean聚类,层次聚类,DBSCAN聚类,谱聚类
"""
import os
os.environ['OMP_NUM_THREADS'] = '4' #设置OMP程序，运行时的线程数，避免任务多并发执行报错
# 导包
from sklearn.cluster import KMeans   #聚类的API ,采用指定质心 来分卒
import matplotlib.pyplot as plt     # 绘图
from sklearn.datasets import make_blobs  #默认会按照高斯分布(正态分布)生成数据集,只需要指定 均值,标准差
from sklearn.metrics import calinski_harabasz_score, silhouette_score  # 评价指标,值越大,聚类效果越好

def demo1():
    # 加载数据
    # 参数1:样本数量  参数2:样本特征数量(2列) 参数3:样本标签数量(3类)  参数4:标准差 参数5:随机种子
    x,y = make_blobs(n_samples=1000,n_features=2,centers=[[-1,1],[0,0],[1,1],[2,2]],
                     cluster_std=[0.4,0.2,0.3,0.4],random_state=23)
    # 2.绘制上述的图形
    plt.scatter(x[:,0],x[:,1])

    # 创建模型
    # 参数1:聚类数量 ,参数2:随机种子
    estimator = KMeans(n_clusters=4,random_state=23)
    # 模型训练及预测
    y_pre = estimator.fit_predict(x)  # 预测值

    # 绘制预测结果
    # 参数1:横坐标 参数2:纵坐标
    plt.scatter(x[:,0],x[:,1],c=y_pre)
    plt.show()

    # 评价指标
    print(f"评价指标(评分):{calinski_harabasz_score(x,y_pre)}") # 越大越好


# 案例： 演示聚类算法的评估指标 即：SSE+肘部法 SC轮廓系数法 CH轮廓系数法
'''
聚类算法的评估指标：
                思路1：SSE+肘部法
                特点：
                   随着K值的增加，SSE值会逐渐减少
                目标：
                    SSE值越小，代表簇内样本越聚集，内聚程度越高
                肘部法：
                    K值增大，SSE值会随之减小，下降梯度陡然变缓的时候，那个K值，就是我们要的最佳值    
                    
                    
误差平方和SSE:
            误差平方和的值越小越好
            主要考虑：簇内聚程度
肘部法：
    下降率突然变缓时即认为时最佳的K值
SC系数：
取值为[-1,1]，其值越大越好
主要考量：簇内聚程度、簇间分离程度

CH系数：
分数s高则聚类效果好
CH达到的目的：用尽量少的类别聚类尽量多的样本，同时获得较好的聚类效果
主要考量：簇内聚程度，簇间分离程度、质心个数      
'''

# 定义函数，演示SSE + 肘部法
def demo2_sse():
    # 定义sse列表，记录：每个k值的SSE值
    sse_list = []
    # 生成数据
    x,y =make_blobs(
        n_samples=1000,
        n_features=2,
        centers=[[-1,1],[0,0],[1,1],[2,2]],
        cluster_std=[0.4,0.2,0.2,0.2],
        random_state = 23
    )
    # for训练遍历，获取到每个K值，计算其对应的sse值，并添加到sse_list列表中
    for k in range(1,20):
        # 创建kmeans对象，参数1：簇的数量 参数2：最大的迭代数 参数3：随机种子 参数4:初始化参数
        estimator = KMeans(n_clusters=k,max_iter=100,random_state=23,n_init=10)
        # 训练模型
        estimator.fit(x)
        # 模型预测
        # 获取到每个簇的sse值
        sse_value = estimator.inertia_
        # 将每个K值对应的sse值，添加到see_list列表中
        sse_list.append(sse_value)

    # 绘制sse曲线 创建画布
    plt.figure(figsize=(10,15),dpi=80)
    # 设置x轴的刻度
    plt.xticks(range(0,20,3))
    # 添加x,y轴标签
    plt.ylabel('sse')
    plt.xlabel('k')
    # 添加网格虚线
    plt.grid()
    # 添加标题
    plt.title("SEE VALUE")
    # 传入数据
    plt.plot(range(1, 20), sse_list)
    plt.show()

# 定义函数，演示SSE + 肘部法
def demo2_sc():
    # 定义sc列表，记录：每个k值的sc值
    sc_list = []
    # 生成数据
    x,y =make_blobs(
        n_samples=1000,
        n_features=2,
        centers=[[-1,1],[0,0],[1,1],[2,2]],
        cluster_std=[0.4,0.2,0.2,0.2],
        random_state = 23
    )
    # for训练遍历，获取到每个K值，计算其对应的sc值，并添加到sc_list列表中
    for k in range(2,20):  # 考虑簇外，至少两个簇
        # 创建kmeans对象，参数1：簇的数量 参数2：最大的迭代数 参数3：随机种子 参数4:初始化参数
        estimator = KMeans(n_clusters=k,max_iter=100,random_state=23,n_init=10)
        # 训练模型
        estimator.fit(x)
        # 模型预测
        y_pred = estimator.predict(x)
        # 获取到每个簇的sc值
        sc_value = silhouette_score(x,y_pred)
        # 将每个K值对应的sc值，添加到see_list列表中
        sc_list.append(sc_value)

    # 绘制sc曲线 创建画布
    plt.figure(figsize=(10,15),dpi=80)
    # 设置x轴的刻度
    plt.xticks(range(0,20,3))
    # 添加x,y轴标签
    plt.ylabel('sc')
    plt.xlabel('k')
    # 添加网格虚线
    plt.grid()
    # 添加标题
    plt.title("SEE VALUE")
    # 传入数据
    plt.plot(range(2, 20), sc_list)
    plt.show()



# 定义函数，演示SSE + 肘部法
def demo2_cv():
    # 定义sse列表，记录：每个k值的SSE值
    sse_list = []
    # 生成数据
    x,y =make_blobs(
        n_samples=1000,
        n_features=2,
        centers=[[-1,1],[0,0],[1,1],[2,2]],
        cluster_std=[0.4,0.2,0.2,0.2],
        random_state = 23
    )
    # for训练遍历，获取到每个K值，计算其对应的sse值，并添加到sse_list列表中
    for k in range(2,20):
        # 创建kmeans对象，参数1：簇的数量 参数2：最大的迭代数 参数3：随机种子 参数4:初始化参数
        estimator = KMeans(n_clusters=k,max_iter=100,random_state=23,n_init=10)
        # 训练模型
        estimator.fit(x)
        # 模型预测
        y_pred = estimator.predict(x)
        # 获取到每个簇的sse值
        cv_value = calinski_harabasz_score(x,y_pred)
        # 将每个K值对应的sse值，添加到see_list列表中
        sse_list.append(cv_value)

    # 绘制sse曲线 创建画布
    plt.figure(figsize=(10,15),dpi=80)
    # 设置x轴的刻度
    plt.xticks(range(0,20,3))
    # 添加x,y轴标签
    plt.ylabel('sse')
    plt.xlabel('k')
    # 添加网格虚线
    plt.grid()
    # 添加标题
    plt.title("SEE VALUE")
    # 传入数据
    plt.plot(range(2, 20), sse_list)
    plt.show()
# 测试
# 测试
if __name__ == '__main__':
    # demo2_sse()
    # demo2_sc()
    demo2_cv()

