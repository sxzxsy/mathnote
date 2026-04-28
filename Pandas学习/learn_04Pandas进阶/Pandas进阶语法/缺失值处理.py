# 缺失值处理
import pandas as pd
import numpy as np
import  os
os.chdir(r'相对路径')  # 修改相对路径的位置

# 解决中文显示问题，下面的代码只需运行一次
import matplotlib as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.reParams['axes.unicode_minus'] =False

# 读取文件数据
movie_df = pd.read_csv('文件路径')
# 查看数据介绍
m1 = movie_df.columns  # 查看所有列名
m2 = movie_df.info   # 查看数据的基本信息
m3 = movie_df.describe()  # 查看数据的统计描述信息（均值，中位值，标准差等等）


# 1.1删除缺失值
movie_df.dropna(axis=0) # 删行  加入Inplace =True 才会修改原数据
movie_df.dropna(axis=1) # 删列

# 2.2判断某列是否有缺失值
pd.isnull(movie_df)  # 判断的是整个df是否为空
pd.notnull(movie_df)  # 判断的是整个df是否不为空
pd.isnull(movie_df['列名'])  # 判断的是整个df
# 判断某列是否是包含缺失值的列
np.all(pd.notnull(movie_df) == False)  # 整列都是True——结果是True ,但凡有Flase,结果是Flase


# 3.3填充缺失值
movie_df.fillna("要填充的值")  # 固定值
movie_df['列名'].fillna(movie_df['列名'].mean())  # 填充每列的平均值

# for循环的方式 使用每列的平均值，填充各列的缺失值
for i in movie_df.columns:   # 拿到所有的列进行判断
    # 判断某列是否有缺失值
    # movie_df[列名]  根据列名 ，找到df中的某个列 ——series对象
    #pd.notnull(某列数据)  判断该列的每个值是否为缺失值，True——不为空，False——为空（缺失值）
    if np.all(pd.notnull(movie_df[i]) == False):
        # 如果有缺失值，进行下列操作
        print(i)  # 输出包含缺失值的列
        # 打印两列的平均值
        print(movie_df[i].mean())
        # 用该列的平均值来填充缺失值
        movie_df[i].fillna(movie_df[i].mean(),inplace=True)
