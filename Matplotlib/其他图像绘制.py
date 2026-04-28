#导包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
os.chdir(r'E:\python-leran\pythonlearn')
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams["axes.unicode_minus"] = False

# # 1. 绘制柱状图 准备画布
# plt.figure(figsize=(10,8),dpi=80)
# # # 2.准备数据
# x = (1,5,7,9,4)  # x轴坐标
# y = (9,4,6,2,7)  # y轴坐标
# plt.bar(x,y)
# # 2.1设置网格
# plt.grid(linestyle = '--',color = 'r',alpha = 0.5)
# # 2.2 设置标题添加信息
# plt.title("柱状简单示例图")
# plt.xlabel("x坐标")
# plt.ylabel("y坐标")
# # 3. 绘图
# plt.show()

# # 2.绘制直方图 适合连续的数据的分布和统计
# # 2.1 准备画布
# plt.figure(figsize=(10,8),dpi=80)
#
# # 2.2 准备数据
# data = np.random.random(500) # 生成100个随机 ——正态分布
# # 2.3 绘制直方图
# plt.hist(data,bins=20,color='g' )  # bins是数量
# # 2.4 绘制网格
# plt.grid(linestyle = "--",color = 'r',alpha = 0.5)
# # 2.5 添加标题及信息
# plt.title("直方图简单示例",fontsize = 20)
# plt.xlabel("x坐标")
# plt.ylabel("y坐标")
# # 2.6 添加图例
# plt.legend(loc = 0)
# # 2.7 显示绘图
# plt.show()

# 3.绘制饼图 适合比例的统计
# 3.1 准备画布
plt.figure(figsize=(10,8),dpi=80)
# 3.2 准备数据
sizes = [25,35,10,5,25]  # 相当于x
labels = ["年入10万","年入5万","年入五十万","年入百万","没有收入"]  # 相当于y
# 3.3 绘制饼图
plt.pie(sizes ,labels=labels,autopct="%1.1f%%" )  # bins是数量
# 3.4 绘制网格
plt.grid(linestyle = "--",color = 'r',alpha = 0.5)
# 3.5 添加标题及信息
plt.title("饼简单示例")
# 3.6 添加图例
plt.legend(loc = 0)
# 3.7 显示绘图
plt.show()


# 4.散点数统计
plt.figure(figsize=(10,8),dpi=80)
# 4.1准备数据
x = [4,7,4,8,2]  # x轴坐标
y = [9,4,6,2,7]  # y轴坐标
# 绘制散点图
plt.scatter(x,y)
# 4.2设置网格
plt.grid(linestyle = '--',color = 'r',alpha = 0.5)
# 4.3设置标题添加信息
plt.title("散点简单示例图")
plt.xlabel("x坐标")
plt.ylabel("y坐标")
# 4.4 绘图
plt.show()



