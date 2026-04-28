# 介绍：Seaborn是一个python 数据可视化，它基于Matplotlib 并且它提供了跟高级的绘图功能
# 在pandas中绘图 只在数据后边直接添加.plot ()
# Seaborn中绘图 是图形名 + plot() 例如histplot()
import sklearn
sklearn.show_versions()
# 导包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # 底层依赖matplotlib

# 设置显示中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置正常显示符合
plt.rcParams["axes.unicode_minus"] = False

# 读取数据
df = pd.read_csv('E:/python-leran/3.数据/tips.csv', index_col=0) #index_col=0 指定第一列作为索引列 离线方式，数据要放在当前目录下
df1 = sns.load_dataset('tips') # 直接从seaborn中加载数据 在线方式，电脑要联网
# 绘图
sns.scatterplot(x='total_bill', y='tip', data=df, hue='sex', style='time', size='size')
print(df1)

