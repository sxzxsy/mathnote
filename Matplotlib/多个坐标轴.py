# 使用面向对象的画图方法
# 语法 ：matplotlib.pyplot.subplots(nrows =  , ncols= , **fig_kw)
# 导包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir(r'E:\python-leran\pythonlearn')
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams["axes.unicode_minus"] = False


# 需求：绘制西安和北京某天一小时内的气温折线图
import random
#1. 准备x，y轴数据
x = range(60)
# 1.1推荐使用列表推导式 语法：[表达式 for 变量 in 迭代器]
y_xian =[random.uniform(15,18)for i in x]  # 要小数.uniform(最小值，最大值)  整数.randint(最小值，最大值)
y_beijing =[random.uniform(10,14)for j in x]

# 2.创建画布 多个坐标轴
# plt.figure(figsize=(10,5),dpi=80)
# 创建多个坐标轴 以元组形式返回结果 即(画布对象,坐标轴对象)
fig , axes = plt.subplots(1,2, figsize=(20,10),dpi=80)

# 开始绘图 axes[0]表示第一个坐标轴中画西安 axes[1]表示第二个坐标轴中画北京
# plt.plot(x,y_xian,color = 'red',label = '西安')
axes[0].plot(x,y_xian,color = 'red',label = '西安')
axes[1].plot(x,y_beijing,color = 'blue',label = '北京')

# 3.1构造x,y刻度及标签 语法：plt.xticks(x刻度值，x刻度标签) plt.yticks(y刻度值，y刻度标签)
x_ticks_label = [f"11点{i}分" for i in x]  # 使用列表推导式设置x轴刻度标签
y_ticks_label = range(40)

# 3.2具体的添加x轴和y轴刻度信息的动作
# plt.xticks(x[::5],x_ticks_label[::5]) # 参数1：x轴刻度值 参数2：x轴刻度标签
# plt.yticks(y_ticks_label[::5]) # 添加y轴刻度标签 步长为5
# 设置左子图（即axes[0]）的刻度标签
axes[0].set_xticks(x[::5],x_ticks_label[::5])
axes[0].set_yticks(y_ticks_label[::5])

# 设置右子图（即axes[0]）的刻度标签
axes[1].set_xticks(x[::5],x_ticks_label[::5])   # 添加set方法
axes[1].set_yticks(y_ticks_label[::5])


# 4添加网格  不用添加set方法
axes[0].grid(linestyle = '-.',color = 'g',alpha = 0.5) # 参数1：网格线样式，参数2：颜色，参数3：透明度
axes[1].grid(linestyle = '-.',color = 'g',alpha = 0.5)

# 5.添加左描述信息    修改描述信息时需要添加set方法
axes[0].set_title("西安市某一天的某个小时的天气气温变化")
axes[0].set_xlabel("时间")
axes[0].set_ylabel("气温")

# 5.添加右描述信息   修改描述信息时需要添加set方法
axes[1].set_title("北京市某一天的某个小时的天气气温变化")
axes[1].set_xlabel("时间")
axes[1].set_ylabel("气温")

# 图例
axes[0].legend(loc = 0)  # 不用添加set
axes[1].legend(loc = 0)
# 展示
plt.show()