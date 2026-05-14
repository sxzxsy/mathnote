# 朴素贝叶斯算法是唯一一个利用概率进行分类的一种机器学习算法
# P(a|b) :表示事件a在事件b已经发生条件下的概率
# 贝叶斯公式：P(A)*P(B|A) =P(B)*P(A|B) = P(AB)
# P(C|W) = P(W|C)P(C) / P(W)  P(C):表示C出现的概率，一般是目标值
# 拉普拉斯平滑系数：为了避免概率值为0，在分子和分母分别加上一个数值，这就是拉普拉斯平滑系数的作用
# 公式：P(F1|C) = Ni+a / N+am
# a:是拉普拉斯平滑系数 一般指定为1  Ni:是F1中符合条件C的样本数量  N：实在条件C下所有样本的总数 m:表示所有独立样本的总数

# 朴素贝叶斯案例：商品评论情感分析
# 导包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB # 多项分布朴素贝叶斯

# 1.读取文件，获取原始数据
df = pd.read_csv("E:/data/书籍评价.csv",encoding='gbk')
# print(df.info())

# 数据预处理
# 添加labels列:充当：标签列 ，好评——>1 差评——>0
df['labels'] = np.where(df['评价'] == '好评',1,0)
# 抽取label列 作为：标签
y = df['labels']
# # 演示jieba 分词
# print(jieba.lcut("好好学习，天天向上，万事顺意，财源滚滚"))
# 对用户的评论信息,做切词
comment_list = [','.join(jieba.lcut(line)) for line in df['内容']]
# 数据格式:['第一条评论切词1,切词2,切词3,......','第二条评论切词1,切词2,......']
# print(comment_list)
# 加载 停用词列,即;里边记录的词,不需要参与模型训练,预测,要被删除的词,例如:的,啊之类
with open('E:/data/stopwords.txt','r',encoding='UTF-8') as src_f:
    # 一次读取所有的行
    stopwords_list = src_f.readlines()
    # 删除最后的"\n"
    stopwords_list = [line.strip() for line in stopwords_list]
    # 对停用词列表去重
    stopwords_list = list(set(stopwords_list))

# 创建向量化对象,从 评论切词列表中 删除停用词 ,并且统计词频(单词矩阵)
transfer = CountVectorizer(stop_words=stopwords_list) # 参数:停用词列表
# 统计词频矩阵 先训练,后转换,再转数据
transfer.fit(comment_list)
# x的格式:[[第1条评论的切词分布,有就是1,没有就是0],[...]]
x = transfer.transform(comment_list).toarray()

# 划分数据集 因为只有13条数据,所以我们按照7:3划分数据集
X_train = x[:10]
X_test = x[10:]

Y_train = y[:10]
Y_test = y[10:]
# X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.3,random_state=23)
# 特征工程(省略)
# 模型训练
estimator = MultinomialNB()
estimator.fit(X_train,Y_train)
# 模型预测
y_pre = estimator.predict(X_test)
print(f"预测结果:{y_pre}")
# 模型评估
print(f"AdaBoost准确率：{accuracy_score(Y_test,y_pre)}")

# 性能提升