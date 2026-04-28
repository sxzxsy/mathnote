# 数据合并

# 准备数据
import pandas as pd

df = pd.read_csv("文件路径")

# 拿数据
df1 = df[:10]
df2 = df[10:20]

# 语法一 pd.concat([列名，列名],axis = 0/1)  既能行合并（参考行索引）也能列合并（参考列明），但是不能指定指定字段 默认外连接方式
# 细节：列合并 参考列名
new_df = pd.concat([df1,df2],axis=0) # 数据列合并（垂直合并）,axis= 1,行合并
# 行合并参考  行索引（值）
new_df1 = pd.concat([df1,df2],axis=1) # 数据行合并（垂直合并）,axis= 0,行合并
# 满外连接
new_df2 = pd.concat([df1,df2],axis=1,join='outer') # 数据行合并（垂直合并）,axis= 0,行合并
# 内连接 只要交集
new_df3 = pd.concat([df1,df2],axis=1,join='inner') # 数据行合并（垂直合并）,axis= 0,行合并


# 语法二df.meager（列名1，列名2，how=inner,on = 关联字段）合并 只能进行左右链接，无法进行上下链接
new_df21 = pd.merge(df1,df2,how='inner',on=['关联字段1','关联字段2'])
# 内连接
new_df32  = pd.merge(df1,df2,how='inner',on=['关联字段1']) # 内连接，on = 关联字段1
# 外连接 指定合并字段
new_df4 = pd.merge(df1,df2,how='outer',on=['关联字段1','关联字段2']) # 满外连接，on = 关联字段1，关联字段2
# 左外连接 = 左表全集+交集
new_df5 = pd.merge(df1,df2,how='left',on=['关联字段1','关联字段2']) # 左外连接
# 右外连接 = 右边全集+交集
new_df6 = pd.merge(df1,'数据2',how='right',on=['关联字段1','关联字段2']) # 右外连接
# merge 第二种写法
df1.merge(df2,how='inner',on='关联字段1')
