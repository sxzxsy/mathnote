# 导包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # 底层依赖matplotlib

# 设置显示中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置正常显示符合
plt.rcParams["axes.unicode_minus"] = False

# 读取数据
df = pd.read_csv('E:/python-leran/3.数据/winemag-data_first150k.csv', index_col=0) #index_col=0 指定第一列作为索引列
# print(df)


# -----------------------------------------------------------------------------
# # 需求1：绘制图像，展示产葡萄酒最多的十个产地信息
# # 查看详细
# # print(df.info())
# # print(df.describe())
# print(df.columns)
# # 'country国家', 'description描述', 'designation葡萄酒酿造厂所在的葡萄园', 'points分数
# # ', 'price价格', 'province葡萄酒来自的省份或者州',
# #        'region_1区域1', 'region_2区域2', 'variety用来制作葡萄酒的葡萄品种', 'winery酿酒的酿酒厂'],
# #       dtype='object')
# 根据产地分组，基于points分数（也可以是其他不包含缺失值的列），进行count统计   ascending=False降序排列
# num = df.groupby('province',as_index=False).points.count().sort_values(by='points',ascending=False)
# print(num[:10])

# # 思路2：value_counts() 值的个数，默认自动降序排列
# df.province.value_counts().head(10).plot.bar(figsize = (10,5),color = ('r','g','b','y','c')) # plot.bar() 绘制柱状图
# df.province.value_counts().head(10).plot() # 绘制折线图
#
# plt.show()
#
# # #############最终写法##############
# # step1:定义变量，记录参数，字典形式
# text_kwargs = dict(figsize = (10,5),color = ('r','g','b','y','c'),fontsize = 15)
#
# # step2:绘制
# df['province'].value_counts().head(10).plot.bar(**text_kwargs)

print("*"* 50)
# -----------------------------------------------------------------------------------
# 需求2 绘制图形，展示葡萄酒最多的10个产地的占比
# 1.统计10个产地的数量 使用分组聚合函数
# n = df.groupby('province',as_index=False).points.count().sort_values(by = 'points',ascending=False).head(10)
# n =df.province.value_counts().head(10)
# # 2.计算每个产地的占比，即：产地产的葡萄酒数量就是count /总共的葡萄酒数量就是整个数据的len  len(df)
# r = n/len(df)
#
# # 3.绘图
# c = dict(figsize = (10,5),color = ('r','g','b','y','c'),fontsize = 15)
# r.plot.bar(**c)
#
# # 展示
# plt.show()


print("*"* 50)
# -----------------------------------------------------------------------------------
# 需求三, 展示每个评分的葡萄酒种类（个数）
n = df['points'].value_counts().sort_index() # value_counts() 表示：统计值的个数
print(n)

# 绘图 设置参数 柱状图
c = dict(figsize = (10,5),color = ('r','g','b','y','c'),fontsize = 15)
n.plot.bar(**c)
plt.show()