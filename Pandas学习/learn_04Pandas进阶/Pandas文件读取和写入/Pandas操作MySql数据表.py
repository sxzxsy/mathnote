# pandas读取mysql数据表操作流程
import pandas as pd
from sqlalchemy import create_engine# 导入引擎对象

"""
    1.前提：你的Anaconda要先安装：pymy sql和sqlalchemy模块
        安装方法：pip install 模块名
    2.你的电脑还需安装mysql数据库

"""
# 要求 把数据写入MySQL数据表
#1. 先准备 写入到mysql数据表中的数据
# index_col=0 的意思是 将csv文件中的第一列作为索引列
data = pd.read_csv("文件地址",encoding="utf-8",index_col=0)

# 2.导包

# 3.创建引擎对象
engine = create_engine("数据库+模块名：//数据库的用户名:密码@主机名:端口号/要操作的数据库名?编码方式")

# 4.具体的往数据库写数据的动作
# 参数1：数据表名,参数2：引擎对象,参数3：如果数据表已经存在，则追加数据，参数4：是否把索引写入数据库
data.to_sql("表名",engine,if_exists="append",index=False)

# 5.提示
print("数据写入成功")

# 6.从数据库读数据
# 参数1：sql语句，参数2：引擎对象
mysql_data = pd.read_sql("表名",engine) # 读取全表
mysql_data1 = pd.read_sql("列名 ,具体到那几段",engine,index_col="索引列") # 读取指定列

