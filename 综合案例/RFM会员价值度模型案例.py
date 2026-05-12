# 导包
import pandas as pd
import numpy as py
import pymysql
import time  # 时间库
from sqlalchemy import  create_engine # 数据库引擎

from pyecharts.charts import Bar3D  #3D柱状图库
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

# 1.-------------------------加载数据--------------------------------
# 1.1定义列表，记录：excel表名
sheet_names = ['2015','2016','2017','2018','会员等级']
# 1.2.从多个excel表中读取数据，获取到的是字典形式——{‘2015':df对象}
# 参数1：excel文件名 参数2：excel文件中的表名
sheet_dict = pd.read_excel('E:/python-leran/3.数据/sales.xlsx',sheet_name=sheet_names)

# 查看sheet_dict数据类型
print(type(sheet_dict)) #<type:dict>

# 查看2015excel的dataframe对象
print(sheet_dict['2015'])  # 类型是DataFrame

# 查看2015excel的dataframe对象的 基本信息
print(sheet_dict['2015'].info())

# 查看2015excel的dataframe对象的 统计信息
print(sheet_dict['2015'].describe())

# 查看字典中每个df对象的 基本信息和统计信息
# step1:遍历，获取到每个sheet表名
for i in sheet_names:
    print(i) # 每个表名
    print(sheet_dict[i].info()) # 查看基本信息
    print(sheet_dict[i].describe()) # 查看统计信息


# --------------------------------数据的预处理------------------------------------
#需要处理的动作：1.删除缺失值 2.过滤出金额>1的数据 3.固定的时间节点（以每年的最后一天作为当年的分析节点）
# for遍历 ，获取到每张表(除了最后一张)
for i in sheet_names[:-1]:
    print(i)  #每个sheet表名
    # 通过sheet_dict[i]到每个表中 ，然后删除缺失值
    sheet_dict[i] = sheet_dict[i].dropna()
    # 过滤出金额>1的数据
    sheet_dict[i] = sheet_dict[i][sheet_dict['订单金额']>1] # 过滤出表中订单金额这一列中金额>1的数据
    # 固定时间节点
    sheet_dict['max_year_date'] = sheet_dict[i]['提交日期'].max()

# 查看处理后的数据
for i in sheet_names:
    print(i)
    print(sheet_dict[i].info())
    print(sheet_dict[i].describe())

# 将excel中的四张表合成一个表     dataframe更换了合并表 换了名称 —— df_merage
# 由于sheet_dict中的数据是字典形式，我现在需要合成表的话，需要的是其中的’‘{‘2015':df对象}’‘df对象。sheet_dict.value获取
# 但是在pandas数据合并中，语法中的数据类型必须是列表（数组），所以需要将字典中的值转换成列表 list(sheet_dict.values())
# 不需要合成最后一张表 list(sheet_dict.values()[:-1])
# pd.concat(list(sheet_dict.values()[:-1]), axis=0)
# df_merge = pd.concat(list(sheet_dict.values()[:-1]), axis=0)

# 合成以后，索引还是各自是各自的，所以我们需要对所以做处理
df_merge = pd.concat(list(sheet_dict.values()[:-1]), axis=0,ignore_index=True)
# ignore_index=True 忽略索引 作用：放弃原有数据自带的索引，改用操作后默认生成的连续整数索引

#   R：最近购买间隔  F：频次  M：金额
# 为了好区分，给DF对象 新增一个 ，year列
df_merge['year'] = df_merge['提交日期'].dt.year # 获取年份 只要年

# 给表新增一列，date_interval 表示本订单购买时间 距统计节点时间的 差值
df_merge['date_interval'] = (df_merge['max_year_date'] - df_merge['提交日期'])#

# 把date_interval列，
df_merge['date_interval'] = df_merge['date_interval'].dt.days



# ---------------------------------------数据统计分析------------------------------------------
# 基于year和会员ID分组 统计：RFM三项的基本数据
# 回顾：RFM: R：最近购买时间  F：频次  M：金额
rfm_gb = df_merge.groupby(['year','会员ID'],as_index=False).agg({  # as_index=False 表示不生成新的索引
    'date_interval':'min', # 最近一次购买时间
    '订单号':'count', # 购买次数
    '订单金额':'sum' # 金额
})
print(rfm_gb)

# 修改列名
rfm_gb.columns = ['year','会员ID','r','f','m']

# 分别查看r f m列的数据分布 通过上边的列名 可以使用切片方法查看[ : ,2:] ——>[行号,列索引]
rfm_gb.iloc[ : ,2:].describe() # 利用df.iloc[ : ,2:] 获取r f m列的数据, 利用describe()查看数据分布



# 划分区间，分别给出：RFM的评分：依据：r 最近一次购买，越小分数越高 f 购买次数，越大分越高  m 购买金额，越大分越高
# 思路1：我们给定区间数 ，由系统自动划分区间范围 pd.cut 参数一：是要划分的值，bins参数二：是区间数
pd.cut(rfm_gb['r'] ,bins=3) # bins=3 划分3个区间 默认是左闭右开 pd.cut()作用：划分区间
pd.cut(rfm_gb['f'] ,bins=3)
pd.cut(rfm_gb['m'] ,bins=3)

# 思路2：我们手动指定区间范围（由于我们使用三分法 需要四个数来划分三个区间，故此区间数也是四个）由系统自动划分区间数
r_bins= [-1,79,255,365] # 这是根据rfm_gb查看列统计信息(describe)中的["r"]结果(min,25%,50%,75%,max)，通过cut包右不包左的规则得来的
f_bins =[0,2,5,130] # 当根据rfm_gb无法确定区间范围时，这个时候我们就需要去向更了解这个东西部门商讨
m_bins =[1,69,1199,206252] # 这是根据rfm_gb查看列统计信息(describe)中的["m"]结果(min,25%,50%,75%,max)，通过cut包右不包左的规则得来的
pd.cut(rfm_gb['r'] ,bins=r_bins) # 根据区间范围，系统自动划分区间数
pd.cut(rfm_gb['f'] ,bins=f_bins)
pd.cut(rfm_gb['m'] ,bins=m_bins)

# 思路3：基于我们手动指定区间范围，给出每个范围的评分（三分法，低中高） 要新增列对每个值给出相应的分数
rfm_gb['r_label'] = pd.cut(rfm_gb['r'],bins=r_bins,labels=[3,2,1]) # 评分标准：r值越小，分数越高
rfm_gb['f_label'] = pd.cut(rfm_gb['f'],bins=f_bins,labels=[1,2,3]) # 评分标准：f值越大，分数越高
rfm_gb['m_label'] = pd.cut(rfm_gb['m'],bins=m_bins,labels=[1,2,3]) # 评分标准：m值越大，分数越高

# ####################思路4 实际开发中的写法#######################
# 思路3：基于我们手动指定区间范围，我们需要手动给出每个范围的评分（三分法，低中高） ‘要新增及格列对每个值给出相应的分数以便于后边直观的统计’
rfm_gb['r_label'] = pd.cut(rfm_gb['r'],bins=r_bins,labels=[i for i in range(len(r_bins)-1,0,-1)]) # 评分标准：r值越小，分数越高
rfm_gb['f_label'] = pd.cut(rfm_gb['f'],bins=f_bins,labels=[i for i in range(1,len(f_bins))]) # 评分标准：f值越大，分数越高
rfm_gb['m_label'] = pd.cut(rfm_gb['m'],bins=m_bins,labels=[i for i in range(1,len(m_bins))]) # 评分标准：m值越大，分数越高



# 我们可以创建一个新的列，将r_label，f_label，m_label列相加，得到RFM的分数，评分标准：分数越高，越重要
# 但是由于r_label，f_label，m_label是int类型，所以需要将r_label，f_label，m_label列转换为字符串类型进行相加操作
rfm_gb['r_label'] = rfm_gb.astype( str) # 将r_label，f_label，m_label列转换为字符串类型
rfm_gb['f_label'] = rfm_gb.astype( str) # 将r_label，f_label，m_label列转换为字符串类型
rfm_gb['m_label'] = rfm_gb.astype( str) # 将r_label，f_label，m_label列转换为字符串类型
# 创建新列表接收r_label，f_label，m_label的拼接
rfm_gb['rfm_add'] = rfm_gb['r_label']+rfm_gb['f_label']+rfm_gb['m_label']
print(f"最终的RFM分数结果是{rfm_gb['rfm_add']}")



# ############################导出结果到Excel/mysql中#######################
# 导出结果到excel中，忽略索引
rfm_gb.to_excel('E:/python-leran/3.数据/sales.xlsx',index=False)

# 导出结果到Mysq中
# 创建引擎
engine =create_engine('mysql+pymysql://root:000000@localhost:3306/rfm_gb? charset = utf-8')
# 导入到数据库MySQL表中
# 参数1：要导入的数据表名，参数2：引擎对象，参数3：如果数据表已经存在，则追加数据，参数4：是否把索引写入数据库
rfm_gb.to_sql('rfm_gb',engine,if_exists='append',index=False)
#查看数据
pd.read_sql('select * from rfm_table',engine)


# ###########################数据可视化#######################
# 准备数据 ,即rfm_add(分组结果评分) ,year(年份) ,  number(评分个数)
display_data = rfm_gb.groupby(['year','rfm_add'],as_index=False).agg({'会员ID':'count'})
# 修改列名
display_data.columns = ['year','rfm_add','number']
