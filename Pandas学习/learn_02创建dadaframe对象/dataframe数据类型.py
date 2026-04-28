# pandas的数据类型
"""
    series中没有info()方法，dateframe中有

"""
import pandas as pd
# dataframe的数据类型
# 日期类型 datetime
import datetime
print(datetime.datetime.now())
print(type(datetime.datetime.now()))
# 创建一个dateframe类型的series
s1 = pd.to_datetime(["2025-12-01","2025-12-02","2025-12-03"])
print(type(s1))

# timedelta类型 计算两个日期之差
s = pd.to_datetime([input("请输入您的年龄:")])
s2 = pd.to_datetime(["2026-03-24"])
delta = s2 - s
print(f"结果是{delta}")

# category类型 用于表示分类数据，通常用于有限集合中的数据类型，
# 这种类型的优点在于节省内存空间，并且对分类数据进行操作时，会更快。
# 创建一个category类型的series
s1 = pd.Series(["1","2","3"],dtype="category")
print(s1)
