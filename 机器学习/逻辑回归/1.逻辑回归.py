# 逻辑回归 = 有监督学习，有特征、有标签，且标签是离散的（分类） = 适用于二分类
# 原理：数据，经过线性回归-->预测值-->通过Sigmoid激活函数映射到[0,1]之间
# -->结合自定的阈值 ，划分 正负样本
"""
逻辑回归：Logistic Regression
    一种分类模型，把线性回归的输出，当作逻辑回归的输入
    输出是（0，1）之间的值
基本思想：
    1、利用线性回归模型f(x)= W^Tx+b根据特征的重要性计算出一个值
    2、再使用sigmoid函数将f(x)的输出值映射为概率值
        1、设置阈值(eg:0.5)，输出概率值大于0.5，则将未知样本输出为1类
        2、否则输出为0类
逻辑回归的假设函数
    h(w) = sigmoid(W^Tx+b)
    线性回归的输出，作为逻辑回归的输入
    逻辑回顾 损失函数 = -极大似然估计函数

    简单来说就是将线性回归得到的预测值 通过激活函数 映射为0~1范围的数值，再结合阈值进行结果预测

"""
import pandas

"""
数学表达式：Loss(L) = ∑ (ylog(p) + (1-y)log(1-p))  
                p = h(w) = sigmoid(W^Tx+b)
                p:表示每个样本被分类正确时的概率值
                y:表示每个样本的真实类别（0或1）
                l = p^y(1-p)^y

损失函数设计思想：预测值为A、B2个类别，真实类别所在的位置，概率值越大越好
我们对损失函数的希望是：当样本是1类别 ，模型预测的p越大越好
                   当样本是0类别，模型预测的(1-p)越大越好
逻辑回归的损失函数：对数似然损失
默认将类别数量少的当做正例


流程操作： 
    1、数据加载
    2、数据预处理
    2.1缺失值处理
    2.2确定特征值，目标值
    2.3分割数据
    3、特征工程（特征预处理）
    4、创建模型（标准化）
    5、模型训练（逻辑回归）
    6、模型预测
    7、模型评估
"""
"""
默认将类别数量少的当做正例
精确率，召回率，F1值（F1-Score）
                预测标签(正例)   预测标签(反例)
   正例(真实标签)： 真正例TP      伪反例：FN   ————(真实值)
   假例(真实标签)： 伪正例FP      真反例TN   ————(预测值)
  精确率= tp/(tp+fp)  召回率：tp/(tp+fn)  F1值 P =(2*精确率*召回率)/精确率+召回率
"""
"""
演示混淆矩阵和精确率，召回率 F1值
 """
# 1、导包
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression    # 逻辑回归模型
from sklearn.model_selection import train_test_split   # 测试集训练集分割
from sklearn.preprocessing import StandardScaler       # 标准化
from sklearn.metrics import accuracy_score             # 模型评估
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score       #混淆矩阵

# 需求：已知有10个样本，6个恶性肿瘤（正例），4个良性肿瘤（反例）
# 模型A预测结果为：预测对了3个恶性肿瘤，预测对了4个良性肿瘤
# 模型B预测结果为：预测对了6个恶性肿瘤，预测对了1个良性肿瘤
# 根据对遇上的数据集，搭建 混淆矩阵，并分别计算模型A ，模型B的精确率 ，召回率，F1值

# 1、定义变量，记录 样本数据集
y_train= ["恶性","恶性","恶性","恶性","恶性","恶性",    "良性","良性","良性","良性"]

# 2、定义变量，记录 模型A的预测结果
y_pre_A = ["恶性","恶性","恶性","良性","良性","良性",   "良性","良性","良性","良性"]

# 3、定义变量，记录 模型B的预测结果
y_pre_B = ["恶性","恶性","恶性","恶性","恶性","恶性",   "良性","恶性","恶性","恶性"]

# 4、用标签标记 正例、反例
label = ["恶性","良性"]
df_l = ["恶性(正例)","良性(反例)"]
# 5、针对于 真实值（y_train）和预测值（y_pre_A）进行混淆矩阵
cm_A = confusion_matrix(y_train,y_pre_A,labels=label)
print(f"混淆矩阵为：{cm_A}")

# 6、为了预测结果更好看，把上述的 混淆矩阵 转换成Dataframe
df_A = pd.DataFrame(cm_A,index=df_l,columns=df_l)
print(f"混淆矩阵为：\n{df_A}")

# 7、针对于 真实值（y_train）和预测值（y_pre_B）进行混淆矩阵
cm_B = confusion_matrix(y_train,y_pre_B,labels=label)
print(f"混淆矩阵为：{cm_B}")

# 8、为了预测结果更好看，把上述的 混淆矩阵 转换成Dataframe
df_B = pd.DataFrame(cm_B,index=df_l,columns=df_l,dtype=float)
print(f"混淆矩阵为：\n{df_B}")


# 9、计算模型A的精确率，召回率，F1值
print(f"模型A的精确率：{precision_score(y_train,y_pre_A,pos_label='恶性')}")
print(f"模型A的召回率：{recall_score(y_train,y_pre_A,pos_label='恶性')}")
print(f"模型A的F1值：{f1_score(y_train,y_pre_A,pos_label='恶性')}")

# 10、计算模型B的精确率，召回率，F1值
print(f"模型B的精确率：{precision_score(y_train,y_pre_B,pos_label='恶性')}")
print(f"模型B的召回率：{recall_score(y_train,y_pre_B,pos_label='恶性')}")
print(f"模型B的F1值：{f1_score(y_train,y_pre_B,pos_label='恶性')}")




