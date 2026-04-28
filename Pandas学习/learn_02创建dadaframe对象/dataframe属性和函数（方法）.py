# dataframe属性
import pandas as pd


"""
    # shape 属性 维度，即：行列数
    # index 属性 索引列  对象.index 修改的是全部的  对象.index[n] 报错
    # data  属性  数据
    # columns 属性 列名
    # values 属性 数据值
    # T 行列转置  对象.T 行变列，列变行 这种属性便于在列表里边查看max/min值
"""

# dataframe 方法

"""
    # 对象.head() 方法 获取文件前几行
    # 对象.tail() 方法 获取文件后几行
    # 对象.info() 方法 查看df对象的信息
    # 对象.describe() 方法 查看df对象的描述性 统计信息
    # rename()  方法 能够精准的修改行列索引值 只有他修改
    # reset_index(drop = False) 重设索引  默认是False不删除原索引，反之True，则删除
    # set_index(keys,drop = True)以某列值设置为新的索引 
       keys:列索引名称或列索引名称的列表
       drop:boolean,default True当作新的索引，删除原来的索引
"""