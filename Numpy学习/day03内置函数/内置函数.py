# 内置函数
import numpy as np
# 创建标准的数组正态分布
arr_1 = np.random.randn(3,5)
# 测试基本函数
print(np.abs(arr_1)) # 绝对值
print(np.ceil(arr_1)) # 向上取整
print(np.floor(arr_1)) # 向下取整
print(np.rint(arr_1)) # 四舍五入

# 矩阵
print(np.multiply(arr_1,arr_1)) # 矩阵乘法(行列数一致)
print(np.divide(arr_1,arr_1)) # 矩阵除法 （行列数一致)

# where
# where函数 作用：如果arr_1>0，给你标记返回一个1，否则返回一个-1
# 类似于python中的if else 能够进行条件判断，返回赋值
print(np.where(arr_1 > 0, arr_1, -arr_1))

# 统计函数
print(np.mean(arr_1)) # 计算均值
print(np.std(arr_1)) # 计算标准差
print(np.sum(arr_1)) # 计算和
print(np.max(arr_1))# 计算最大值
print(np.min(arr_1))# 获取最小值
print(np.prod(arr_1))# 获取乘积
print(np.cumsum(arr_1))# 获取累计和
print(np.cumprod(arr_1))# 获取累计积
print(np.percentile(arr_1,50))# 获取百分比
print(np.median(arr_1))# 获取中位数

# 去重函数
print(np.unique(arr_1)) # 去重

# 排序函数
# 通过np.sort返回一个副本
print(np.sort(arr_1)) # 排序
# 通过数组对象.sort () 直接修改原数组
arr_1.sort()
print(arr_1)

# 逻辑函数
print(np.argmax(arr_1))# 获取最大值的索引
print(np.argmin(arr_1))# 获取最小值的索引
print(np.sort(arr_1))# 排序
print(np.argsort(arr_1))# 获取排序后的索引
print(np.any(arr_1))# 判断是否有True
print(np.all(arr_1))# 判断是否有False
print(np.invert(arr_1))# 逻辑取反
print(np.logical_and(arr_1,arr_1))# 逻辑与
print(np.logical_or(arr_1,arr_1))# 逻辑或
print(np.logical_xor(arr_1,arr_1))# 逻辑异或
print(np.logical_not(arr_1))# 逻辑非
print(np.isfinite(arr_1))# 判断是否是有限的
print(np.isinf(arr_1))# 判断是否是无穷大
print(np.isnan(arr_1))# 判断是否是NaN
print(np.isclose(arr_1,arr_1))# 判断是否相等
print(np.iscomplex(arr_1))# 判断是否是复数
print(np.isreal(arr_1))# 判断是否是实数
print(np.iscomplexobj(arr_1))# 判断是否是复数对象
print(np.isrealobj(arr_1))# 判断是否是实数对象
print(np.isfortran(arr_1))# 判断是否是fortran数组
print(np.isneginf(arr_1))# 判断是否是负无穷大
print(np.isposinf(arr_1))# 判断是否是正无穷大
print(np.isneginf(arr_1))# 获取负无穷大的索引
print(np.isposinf(arr_1))# 获取正无穷大的索引
print(np.isneginf(arr_1))# 获取负无穷大的索引
print(np.where(arr_1))# 获取满足条件的索引