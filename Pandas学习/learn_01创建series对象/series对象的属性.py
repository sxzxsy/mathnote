# series对象的属性
# 构建series对象，索引：A-F 值：0-5
import pandas as pd

s6 = pd.Series(data=[0,1,2,3,4,5],index=['A','B','C','D','E','F'])
print(s6)
# 加入列表推导式
s7 = pd.Series([i for i in range(6)],index=[i for i in "ABCDEF"])
print(s6)

# 获取series的索引列
print(s6.index)

# 获取series的值列
print(s6.values)

# series支持根据索引 获取元素 即：series对象[索引值]
print(s6['A'])
