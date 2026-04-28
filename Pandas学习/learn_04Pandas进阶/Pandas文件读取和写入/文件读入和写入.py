import pandas as pd

# pandas中的文件读取操作
# 1.加载文件
df = pd.read_csv("文件地址")
print(df)

# 2.查看文件信息
print(df.info())

# 3.查看文件描述信息
print(df.describe())

# 4.文件写入
df.to_csv("文件地址",index=False)
