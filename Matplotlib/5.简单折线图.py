import matplotlib.pyplot as plt
import numpy as np

# 0. 准备数据
x = np.linspace(-10,10,1000) # 等差
y = np.sin(x)  # 正弦函数

# 1. 创建画布
plt.figure(figsize=(10,15),dpi=80)

# 2.绘制
plt.plot(x,y)

# 3.添加网格
plt.grid()

# 4.显示
plt.show()