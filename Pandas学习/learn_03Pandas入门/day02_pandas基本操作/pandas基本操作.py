###### 加载数据
import pandas as pd


# 1.加载文件
df = pd.read_csv("文件地址")

# 2.移除不需要的字段
df.drop(columns="输入要移除的列名" ,axis = 0 ,inplace=True) # 0:列 1：行

# 3.查看处理后的信息
print(df)
print(df.info()) #查看详细信息
print(df.describe()) # 查看描述统计信息

###### 索引操作
# 根据行列索引获取元素   先列后行
message_01 = df["列名","行名"]

# 结合loc 根据：行索引和列名 来 获取元素
# 格式; df.loc[行索引 ,列名]
# 格式: df.iloc[行索引（行号），列索引]

# 获取表中多行多列元素
# 格式： df，loc["开始的行索引":"结束的行索引","列名1，列名2"]
# 集和iloc来获取多行多列的元素
# df.iloc["行号1":"行号2", "列索引1":"列索引2"]
# 值得一提的是 一般情况下，不自主定义的情况下，行索引是名称，行号是看不见的0123...
#列名就是列名，列索引就是看不见的0123.....


###### 赋值操作
# 按多个键进行排序
# df["列名"] = ”你要赋的值“
# df.low = "你要赋的值"  # 效果同上，更简单，但若是字段有空格，则容易报错


#### 排序操作
# 查看原数据，可以再次运行重新加载的程序
# df.sort_values = (by = ["字段名"],ascending = False) # 降序
# df.sort_values = (by = ["字段名"],ascending = Ture) # 升序
# df.sort_values = (by = ["字段名"，"字段名"],ascending = [Ture,Ture]) # 升序
df.sort_values(by = ['name'],ascending= False)
# 按照索引排序
df.sort_index(ascending=True)  # 默认升序 Ture

# 演示series也有排序方法 sort_index() ,sort_values()
# df.open可以转换为series  ###
s = df.open.sort_index(ascending=True) # 升序操作
print(type(s))

