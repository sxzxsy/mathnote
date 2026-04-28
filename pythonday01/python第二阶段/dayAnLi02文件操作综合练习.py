# 打开文件
date_r = open("WJ ","r",encoding="utf-8")
date_w = open("WJ ","w",encoding="utf-8")

# 文件操作
# 进行数据清洗与筛选
for line in date_r.readlines(): # for循环来接收文件内容
    line =line.strip # 删除文件中的前后空格以及换行符
    if " " == line.split(" ,")[4]:
        # 通过分割方法split将文件中的内容进行分割来进行后续的判断
        # 对数据进行分割来进行比对
        continue

    date_w.write(line + "\n") # 文件写出
    # 由于前边以及使用strip去掉换行符来进行操作
    # 所以当输出的内容需要换行时
# 关闭文件
date_r.close()
date_w.close()