# 文件写入 写入缓冲区
# 打开文件的时候，若打开了一个不存在的文件进行写入
# 那么将会以此创建一个新的文件
# 文件.write(要写入的内容\n) 不会自动换行，得自己加
import time

# 打开 文件
f = open("E:/f.txt", "w" ,encoding="utf-8")

# 写入内容
f.write("哈哈哈哈哈哈")
# 内容刷新 将缓冲区的内容，写入硬盘（文件）中
# 文件.flush()
f.flush()
time.sleep(10) # 表示设置的时间为10s
# 文件关闭 当使用close时，就相当于使用flush刷新。
# 所以当调用close时，可以不使用flush
f.close()

# 文件追加 a模式  也是三大件 ： 打开 ，操作 ， 关闭
# 同样文件不存在时，进行追加操作，也会创建新的文件
f = open("E:/f.txt", "a" ,encoding="utf-8")

# 只有文本文件可以 r w a
# 非文本文件必须带有b模式，以二进制模式处理
f = open("E:/f.txt", "rb" ,encoding="utf-8")
f = open("E:/f.txt", "wb" ,encoding="utf-8")

f.close()
f.close()