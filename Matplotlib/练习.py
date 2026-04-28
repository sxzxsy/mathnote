# 导包
import pandas as pd
import numpy as np
import os
os.chdir(r'E:\python-leran\pythonlearn\data')

import matplotlib.pylab as plt

from pylab import mpl
# 设置显示中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 设置正常显示符合
mpl.rcParams["axes.unicode_minus"] = False


# 绘制某城市中午11点-12点的气温变化图
# 1.创建画布
plt.figure(figsize=(10,8))
import random
# 2. 准备数据
x = range(60) # x轴刻度
y_xian = [random.uniform(2,18)for i in x] # y轴刻度 列表推导式 生成随机数气温
y_beijing = [random.randint(7,30) for j in x]
z_nanjing = [random.randint(5,15)for k in x]

# 3.准备绘图 四个城市
plt.bar(x,y_xian,color = 'red',label = '西安')
plt.bar(x,y_beijing,color = 'blue',label = '北京')
plt.bar(x,z_nanjing,color = 'y',label = '南京')

# 4.添加刻度标签，添加描述信息
# 4.1 构造x刻度标签
x_ticks_label = [f"11点{i}分" for i in x]  # 使用列表推导式 括号不是()是[]  设置x轴刻度标签
y_ticks_label = range(40) # 使用range生成y轴刻度标签
# 4.2 具体添加刻度标签和描述信息
plt.xticks(x[::5],x_ticks_label[::5]) # 参数1：x轴刻度值 参数2：x轴刻度标签 步长为5 标签刻度必须和原刻度一致
plt.yticks(y_ticks_label[::5]) #  参数2：y轴刻度标签 步长为5

# 5. 添加标题
plt.title("中午11点-12点气温变化图")
plt.xlabel("时间") # 添加x轴标题
plt.ylabel("气温") # 添加y轴标题

# 添加网格
plt.grid(linestyle = '-.',color = 'g',alpha = 0.5)
# 添加图例
plt.legend(loc = 0)

# 6.结果显示
plt.show()