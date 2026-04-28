# 导包
import pandas as pd
import os

# 分组聚合， pandas的重点
# 先读取文件
df_data = pd.read_csv('E:/python-leran/3.数据/uniqlo.csv')
print(df_data)

# 1.1 分组聚合：
# """
#     格式：df.groupby(['分组字段1'，'分组字段2',.....]).agg({'列名1':'聚合函数',....})
#     这段代码的作用是：按照指定的字段进行分组，然后对分组后的数据进行聚合
# """
# 需求1 ，按照单列分组
df1 = df_data.groupby(['city'])
print(df1)
print(df1.groups) # 拿到分组后的数据
# 需求2，按照多列分组
df2 = df_data.groupby(['city','channel'])
print(df2)
# 需求3.如何获取某个分组的数据
df3 = df_data.groupby(['city','channel']).get_group(('北京','线下'))
print(df3)

# 需求4.如何获取某个分组的统计数据 重点
# 写法1：通用版本 着重记住
# 根据城市 和渠道分组，计算销售金额 总和
df4 = df_data.groupby(['city','channel']).agg({'revenue':'sum'}) # 返回的是dataframe对象
print(df4)
# 写法2:
df5 = df_data.groupby(['city','channel']).revenue.sum()  # 返回的是series对象
print(df5) # 结果同上

# 需求5.分组 + 聚合  根据城市和销售渠道分组 计算销售金额，订单数量 总和
df6 = df_data.groupby(['city','channel']).agg({'revenue':'sum','order':'sum'})
print(df6)