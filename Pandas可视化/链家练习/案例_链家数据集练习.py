# 导包
import pandas as pd
import numpy as np
import os
os.chdir(r'E:\python-leran\pythonlearn\data')

# 记载数据集
data = pd.read_csv('E:/python-leran/pythonlearn/data/LJdata.csv')
df = pd.DataFrame(data) # 修改数据集名称为df
print(df)

# 1.1修改列名为英文
n = df.columns = ['district', 'address', 'title', 'house_type', 'area', 'price', 'floor', 'build_time', 'direction', 'update_time', 'view_num', 'extra_info', 'link']
print(n)

# # 1.2查看前5行数据
# df1 =df[:5]
# print(df1)
#
# # 1.3查看列数据分布
# df2 = df.info()
# print(df2)
#
# # 1.4 查看列统计指标
# df3 = df.describe()
# print(df3)
#
# # 1.5 查看形状
# df4 = df.shape
# print(df4)
#
# print("—" * 50)

# # 具体的需求
# # 1. 找到租金最低，和租金最高的房子
# df_1 = df.sort_values(by='price').head(1) # 最便宜的
# df_2 = df.sort_values(by='price').tail(1) # 最贵的
# print(df_1)
# print(df_2)
# # 思路2
# df_1_1 = df[df.price ==df.price.min()]
# df_1_2 = df[df.price ==df.price.max()]
# print(df_1_1)
# print(df_1_2)
# # 思路三
# df.nlargest(1,'price') # 它的语法是:  df.nlargest(n,column) n代表前几名 最大的n ，column代表排序的列
# df.nsmallest(1,'price') # 它的语法是:  df.nsmallest(n,column) n代表前几名 最小的n ，column代表排序的列
#
# # 2. 找到最近新上的10套房源
# df_3 = df.sort_values('update_time')
# print(df_3[:10])
# # # 思路2
# # df.nlargest(10,'update_time')
# # df.nsmallest(10,'update_time')
#
# # 3. 查看所有更新时间
# df_4 =df['update_time'].unique() # 去重
# print(df_4)

# 4. 查看看房人数的平均值, 最大值, 最小值
df_5 = df.view_num.agg(['mean','max','min'])
print(df_5[:4])
# 思路二
n =df.view_num.mean()   # df[['view_num']].mean() # dataframe类型的平均值
print(f"mean:{n}")
m =df.view_num.max()
print(f"max：{m}")
p =df.view_num.min()
print(f"min:{p}")


# 5. 查看不同看房人数的房源数量，as_index = False 分组字段不作为行索引（默认为True)
# 思路：基于看房人数分组，统计房源数量
df_6 = df.groupby('view_num',as_index = False).agg({'address':'count'})
print(df_6)
df6_1 = df_6.columns = ['view_num','house_count']
print(df6_1)
# 思路
df.groupby('view_num').address.count()
df.groupby('view_num')['address'].count()
df.groupby('view_num').agg({'address':'count'})


# 6. 查看房租价格的分布, 例如: 平均值, 标准差, 中位数...
df_7 = df.describe()
print(df_7)
# 手动版
# df.price.mean()
# df.price.std()
#df.price.median()


# 7. 找到看房人数最多的朝向
# 思路：基于朝向分组，统计看房人数的总和
df_8 = df.groupby(['direction'],as_index= False).agg({'view_num':'sum'})
df_9 = df_8.sort_values('view_num',ascending=False).head(1) # 按 address字段降序排列
print(df_9)


# 8. 查找最受欢迎的房型
# 思路：基于户型分组，统计看房人数的总和
df_10 = df.groupby(['house_type'],as_index= False).agg({'view_num':'sum'})
df_11 = df_10.sort_values('view_num',ascending=False).head(1)
print(df_11)

# 9. 查找房子的平均租房价格 （元/平米）
# 思路;计算每套房子的平均价格，然后统计所有平均价格的平均值
df['price_area_m²'] = df.price/df.area # 新增一列
print(df)
df_12 = df['price_area_m²'].mean()
print(f"均价{df_12}")

# 10. 找到出租房源最多的小区
# 思路 基于地址（小区）分组，统计房源数量，获取最大值
df_13 = df[['address','view_num']].groupby('address',as_index=False).count()
print(df_13) # 统计房源数量
# 思路二：
df_14= df[['address','view_num']].groupby('address',as_index=False).agg({'view_num':'count'})
print(df_14)  # 统计房源数量  通过df.sort_values 获取房源数量中的最大值
df_15 = df_14.sort_values('view_num',ascending=False).head(1) # False降序
print(df_15)

