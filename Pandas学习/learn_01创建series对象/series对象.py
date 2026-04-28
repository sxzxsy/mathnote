# Pandas中有两大核心数据结构：DataFrame和Series
"""
    其中series（一维表格），DataFrame(二维表格，多列数据)
    serise 列（行）对象， DataFrame 二维表对象，由多个series组成
    """

# 导包
import pandas as pd
import numpy as np
# 创建series对象  series本身自带有索引
# series对象创建时，里边要么是数组，要么是字典，要么是元组，要么是numpy数组，不能混合使用
# 不能不使用类型，否则会报错
s1 =pd.Series([1,2,3])
print(s1)

# 自定义索引
s2 = pd.Series([1,2,3],index=["a","b","c"])
print(s2)


# 使用字典或者元组创建series对象
s1 = pd.Series({1:'a',2:'b',3:'c'})
print(s1)

# 使用元组创建series对象
s3 = pd.Series((1,2,3),index=["a","b","c"])
print(s3)

# 使用numpy形式创建series对象
s4 = pd.Series(np.arange(5))
print(s4)