# numpy的属性介绍
"""
numpy:主要用于数组计算，numpy的数组是ndarray
特点:执行速度快，节省空间
ndarray的下标从0开始，且数组里的所有元素必须是同类型
"""
import numpy as np

# 创建一个数组
# np.arange()创建一个等差数列相当于python的range()
# np.random.rand()创建一个随机数相当于python的random.random()
arr_1 = np.arange(9).reshape(3,3)   # .reshape(x,y)的意思是转换为3行3列的数组
print(arr_1)

# 轴
print(arr_1.ndim)  #2
# 维度
print(arr_1.shape) #(3, 3)
# 元素个数
print(arr_1.size) #9
# 元素占用的字节数
print(arr_1.itemsize) #8
# 数据类型
print(arr_1.dtype) #int64
# 元素类型
print(type(arr_1)) ##<class 'numpy.ndarray'>


# 创建一个python列表
my_list=[1,2,3,4,5]
# 将python列表转换 ndarry对象
arr2 = np.array(my_list)
# 打印
print(arr2) #
# 打印类型
print(type(arr2)) #<class 'numpy.ndarray'>