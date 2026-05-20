import datetime
import numpy as np
import pandas as pd



# 该工具类的目的：对数据做预处理——>时间格式化，按照时间升序排列，且对数据去重
# 数据集在 data目录下的train.csv文件中 ——>拆分训练集和测试集
# 测试集在 data目录下的test.csv文件中 ——>模拟项目上线后，真实的测试集

# 定义函数，data_preprocessing()，对数据集进行预处理操作
def data_preprocseeing(file_path='../data/train.csv'):
    # 1.加载数据
    df = pd.read_csv(file_path)
    # # 将time列转换为datetime类型
    # df['time'] = pd.to_datetime(df['time'])

    # 2.时间格式化转为，%Y-%m-%d %H:%M:%S  字符串类型的time
    df['time'] = pd.to_datetime(df['time']).dt.strftime('%Y-%m-%d %H:%M:%S')
    # # 3.按照时间做排序  参数1： 列名
    df.sort_values('time',ascending=True,inplace=True)
    # 4.去重
    df.drop_duplicates(inplace=True)
    # 5.返回处理后的数据
    # df.info()
    return df


# 测试
if __name__ == '__main__':
    data_preprocseeing()
