# 文件写入到mysql
# 导包
import pandas as pd
from sqlalchemy import create_engine # 导入引擎对象
import numpy as np

# 1.读取文件
df = pd.read_csv("E:/test1/1000kV01.csv")
# print(df.info()) # 查看文件信息
# print(df.describe()) # 查看文件描述信息

# 创建数据引擎
engine = create_engine("mysql+pymysql://root:000000@localhost:3306/learn01?charset=utf8")

# 从查看csv文件来看，数据中存在大量的整列数据为空的列，所有进行数据操作
for i in df.columns:
    # 判断列数据是否为空
    if np.all(df[i].isnull()) == True: # 判断整列数据是否为空 True 表示为空
        # 删除整列数据为空的列
        df.drop(i,axis=1,inplace=True)
# 将csv文件导入到mysql的learn01数据库中
df.to_sql('1000kV01',engine,if_exists='replace',index=False)
print("写入成功")

