# 创建一个数组
# 导入numpyde的包
import  numpy as np

# 创建一个数组 语法：np.astype(dtype)

arr_1 = np.arange(1,10,dtype=np.int64)
print(arr_1)
# 查看数据类型
print(arr_1.dtype)
# 将数组转换成float64
arr_2 = arr_1.astype(np.float64)
print(arr_2)
# 查看转换后的数据类型
print(arr_2.dtype)

# 数组的等比数列 np.logspace(开始值,结束值,元素个数)
# 创建一个等比数列，从1开始，结束值为10，元素个数为10
arr_2 = np.logspace(1,10,10)
print(arr_2)
print(arr_2.dtype)

# 创建一个等差数列 np.linspace(开始值,结束值,元素个数)
# 创建一个等差数列，从1开始，结束值为10，元素个数为10,参数4 是否包含结束值，默认为True。参数5类型
arr_3 = np.linspace(1,10,4,endpoint= False,dtype=np.int64)
print(f"等差数列的结果{arr_3}")
print(arr_3.dtype)





