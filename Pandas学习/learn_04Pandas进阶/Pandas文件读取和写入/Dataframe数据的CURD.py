# dataframe数据的增删改查
#导包
import pandas as pd

# 1.加载数据
df = pd.read_csv("文件地址")
print(df)

# 2.从原始数据集中，拷贝一份出来，做操作
df1 = df[:5].copy()  # 拷贝5行数据




# 3.增加
# 通过直接赋值方式添加列
df["new_column"] = "新列的值" # 写法1 直接新增
df['c1'] = ['xck','scd','dsvs','cava'] # 写法2 传入列表
df['c3'] = df.year *2 # 写法3 通过已有的列series来计算新列的值
def fun_c():
    return  2000
df['c4'] = fun_c() # 写法4 通过函数来计算新列的值

# 3.1 通过assign()函数 新增一列
df = df.assign(new_column = "新列的值")
# 通过assign()函数，新增n列
df.assign(
    c1 = ['xck','scd','dsvs','cava'],
    c3 = df.year *2,
    c4 = df.apply(fun_c,axis=1)
)


# 删除与去重
# drop删除 行数据，除非指定Index= Ture，否则不会修改数据
df.drop(index = [0],inplace=True)  # 根据index来删除行,会修改原始数据

# 删除行 del关键字
del df['列名']    # 删除列
del df[['列名1','列名2','列名3','......']]  # 删除多个列

# 删除列————drop函数
df.drop(columns = ['列名1','列名2','列名3','......'],inplace=True)


# 去重
# 场景1.DataFrame对象，默认只根据列名进行去重
# 场景2.Series对象去重，以 列 做单位进行比较
df.country.drop_duplicates()
df.drop_duplicates(inplace=True) # 语法drop_



# 修改
# 修改某列值
df['列名'] = ['1','2','3','4','5']  #直接修改原数据
# 采用replace()方法 替换
# df.'列名.'replace('修改的数据',inplace  = True)  # 加了inplace=True 会修改原数据


# 查询
# 获取前几条数据
df.head(3) # 获取前3行数据
# 获取后几条数据
df.tail(3) # 获取后3行数据
# 根据列名获取数据
nu = df['列名']  # 获取列名为列名的数据  series对象
nu1 = df[['列名']] # 获取列名为列名的数据 dataframe 对象
# 根据行索引获取数据
nu2 = df.loc['行索引'] # 获取行索引为行索引的数据
# 获取多列封装成dataframe对象
nu3 = df[['行索引1','行索引2']] # 获取行索引为行索引1和行索引2的数据 dataframe对象

# 需求:查询 中，美，日三国2015-2019的数据
# df.query('列名 in ["中国","美国,"日本"] and year in [2015，2016，2017，2018，2019])


# 排序
df.sort_values('列名',ascending=True) # 根据列名排序
df.sort_index(ascending=False) # 根据行索引排序，降序



# rank() 函数 ，类似于sql的窗口函数