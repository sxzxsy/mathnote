# 交叉表和透视表
import pandas as pd

# 交叉表（了解）
# 创建一个实例数据集
data = {
        '性别': ['男', '女', '男', '女', '女', '男'],
        '购买':['是','否','是','是','否','是'],
        '金额':[100,150,200,130,160,120]}
df = pd.DataFrame(data)
print( df)
# 创建交叉表 语法：pd.crosstab(df['字段名'],.....)
# 
df1 = pd.DataFrame(df['性别'],df['购买'])
print(df1)

# 透视表 语法：df.pivot_table(index='行索引',columns='列索引',values='值',aggfunc='聚合函数')
# 作用：统计分组数据，简化分组聚合写法
df2 = df.pivot_table(index='性别',columns='购买',values='金额',aggfunc='mean')
# df3 =df.groupby(['性别','购买']).agg({'金额':'mean'})   #分组聚合 类似于转置
print(df2)

# 交叉表：计算一列数据对于另外一列数据的分组格数
# 透视表: 计算分组数据，简化分组聚合写法，指定某一列对另一列的关系
