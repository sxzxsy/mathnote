# dataframe对象  创建dadaframe对象
import pandas as pd
import numpy as np
# 通过字典和列表创建
# 准备数据集  每个键值对 = 一列数据
data = {
    '日期':['2025-12','2026-01','2026-02'],
    '温度':[25,26,27],
    '天气':['多云','晴朗','多云']
}
# 创建对象
d1 = pd.DataFrame(data)
print(d1)


# 通过元组和列表创建对象
# 准备数据集，每个列/元组 = 一行数据
info = (['索旭哲','男',25],
        ['薛思雨',"女",22],
        ['刘亦菲','女',39])
infd = [1,2,3]
infa = ["name","gender","age"]
# 创建对象
d2 = pd.DataFrame(data=info,index=infd,columns=infa)
print(d2)

# 创建numpy的ndarray对象
arr1 = np.arange(12).reshape(3,4)
print(arr1)

# 把上述的数组封装成dataframe
d3 = pd.DataFrame(data=arr1)
print(d3)

print(d3.shape)