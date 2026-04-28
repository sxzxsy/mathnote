"""
    常见图像绘制 官方网址
    https://matplotlib.org/stable/gallery/index.html
"""

# 初始
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pylab import mpl
# 设置显示中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 设置正常显示符合
mpl.rcParams["axes.unicode_minus"] = False

# 图片保存路径
import os
os.chdir(r'E:\python-leran\pythonlearn')

#
#
# # 绘制北京近一周的气温折线图
# # 回顾可视化步骤 ：1.创建画布 2.准备数据（x轴，y轴） 3.具体的绘图
# # 1.创建画布
# plt.figure(figsize=(10,5),dpi=80) # 设置画布大小 figsize=(宽，高) dpi=画布分辨率
#
# # 2.准备数据 x轴 y轴
# plt.plot([1,2,3,4,5,6,7],[15,11,17,20,24,16,18])# x轴 y轴
# # 2.1 其他操作，例如 添加标题，添加标签，添加网格线，添加注释
# # plt.title('北京近一周气温折线图') # 添加标题
# # plt.xlabel('日期') # 添加标签
# # plt.ylabel('气温') # 添加标签
# plt.grid() # 添加网格线
#
# # 3.绘图
# plt.show()
#

print("-"*50)

# 需求：绘制西安某天一小时内的气温折线图
import random
#1. 准备x，y轴数据
x = range(60)
# 1.1推荐使用列表推导式 语法：[表达式 for 变量 in 迭代器]
y_xian =[random.uniform(15,18)for i in x]  # 要小数.uniform(最小值，最大值)  整数.randint(最小值，最大值)
# 2.创建画布
plt.figure(figsize=(10,5),dpi=80)

# 开始绘图
plt.plot(x,y_xian,color = 'red',label = '西安')

# 3.1构造x,y刻度及标签 语法：plt.xticks(x刻度值，x刻度标签) plt.yticks(y刻度值，y刻度标签)
x_ticks_label = [f"11点{i}分" for i in x]  # 使用列表推导式设置x轴刻度标签
y_ticks_label = range(40)

# 3.2具体的添加x轴和y轴刻度信息的动作
plt.xticks(x[::5],x_ticks_label[::5]) # 参数1：x轴刻度值 参数2：x轴刻度标签
plt.yticks(y_ticks_label[::5]) # 添加y轴刻度标签 步长为5

# 4添加网格
plt.grid(linestyle = '-.',color = 'g',alpha = 0.5) # 参数1：网格线样式，参数2：颜色，参数3：透明度

# 5.添加描述信息
plt.title("西安市某一天的某个小时的天气气温变化")
plt.xlabel("时间")
plt.ylabel("气温")

# 展示
plt.show()