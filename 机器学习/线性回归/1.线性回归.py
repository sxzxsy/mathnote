"""
线性回归（Linear Regressor）
    概述/目的：
        用线性公式 来描述多个自变量（特征）和一个因变量（标签）之间 关系的，对其关系进行建模，基于特征预测标签
        线性回归属于：有监督学习，有特征，有标签，且标签连续
    分类：
        一个特征列+一个标签列的叫一元线性回归 ：y=wx+b (x = x_train和x_test ，y=Y_train和y_test)
        多个特征列+一个标签列的叫多元线性回归:y=w1*x1 +w2*x2+......+wn*xn+b = w^T x +b
    公式：
        一元线性回归 ：y=wx+b (x = x_train和x_test ，y=Y_train和y_test)
            w(机器学习中叫权重，数学中叫斜率)   b(偏置)
        多元线性回归:y=w1x1+w2x2+w3x3+...+wnxn + b
                    =w^T x +b
        (矩阵相乘的条件是行列数一致，两矩阵相乘，矩阵1的行数=矩阵2的列数才能相乘)
矩阵相关：
    1范数 = 向量中各元素 绝对值之和
    2范围 = 向量的模长 ，即：各个元素平方和，开平方根
"""
# 演示线性回归API
from sklearn.linear_model import LinearRegression

# 准备数据
x_train = [[160],[166],[172],[174],[180]] # 训练集特征
y_train = [56.3,60.6,65.1,68.5,75] # 训练集标签
x_test = [[176]] # 测试集特征
# 特征预处理
# 特征工程（特征提取，特征预处理）

# 创建模型
eistmator = LinearRegression()  # LinearRegression() 线性回归模型
eistmator.fit(x_train,y_train)

# 查看斜率和截距
print(f"斜率：{eistmator.coef_}")
print(f"截距：{eistmator.intercept_}")

# 模型预测
y_per = eistmator.predict(x_test)
print(f"预测结果为：{y_per}")