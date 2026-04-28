# 导包
import pandas as pd


# 加载数据
df = pd.read_csv('E:/python-leran/3.数据/uniqlo.csv')



# 1 分组过滤：
# 语法：df.groupby(['分组字段1'，'分组字段2',.....]).filter(lambda x: x['列名'].聚合函数条件)

# 1.1 需求 ：按照城市分组，查询每组销售额平均值大于200的全部数据
df1 = df.groupby(['city']).revenue.mean()
# 1.2 需求：按照城市分组，查询上海的数据
df2 =df.groupby('city').get_group('上海')
# 1.3 需求：按照城市分组，查询每组销售额平均值大于200的全部数据
df3 = df.groupby(['city']).filter(lambda x:x.revenue.mean()>200)
df4 = df.groupby(['city']).revenue.filter(lambda x:x.mean()>200)
