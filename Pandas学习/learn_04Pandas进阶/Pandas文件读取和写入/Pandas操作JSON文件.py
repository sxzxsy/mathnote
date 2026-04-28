# JOSN是一种数据交换格式
# pandas.read_json(path_or_buf, orient=None, typ='frame', lines=False )
# 将JSON格式准换成默认的Pandasn DataFrame格式
# orient参数:string, Indicates of expected JSON string format.
    # split:dict like{index->[index],columns->[columns],data->[data]}
        # split将索引总结到index中，列名总结到columns中，数据总结到data中
    # 'records':list like [{column ->value},......,{column ->value}]
        # records将索引作为字典的key，列名作为字典的value ,以columns：values的形式输出
    #‘index’：dict like{index ->{column ->value}}
        # index将索引作为字典的key，列名作为字典的value，数据作为字典的value 形式：index:{columns:values}
    # ‘columns’：dict like{column ->{index ->value}}
         # columns将列名作为字典的key，索引作为字典的value，数据作为字典的value 形式：columns:{index:values}
    # ‘values’：just the values array
         # values直接输出
    # lines:boolean, default False
         # True:输出每行数据，False:输出所有数据
    # typ:default ‘frame’,指定转换成的对象类型DataFrame或者 Series

import pandas as pd
# 1.读取JSON文件
# 参数1 ： 文件路径。 参数2：orient="records" 表示将JSON数据转换成行记录 ，参数三：lines=True 表示JSON文件中每行是一个JSON对象
json_data = pd.read_json("文件地址",orient="records",lines= True)
print(json_data)
# 2.把数据写入JSON文件中
# json_data.to_json("要写入的文件地址",orient="records") # 结果是列表套字典
json_data.to_json("要写入的文件地址",orient="records",lines=True) # 结果是{},{}....
# json_data.to_json("要写入的文件地址") # 结果是{ { } }
print("写入成功")