
# 实操
count = 0
# 打开文件
f = open("E:/f.txt", "r" ,encoding="utf-8")

#  ###三种方法中，当文件已经读取过一次以后，后边的方法无法再继续读取

#读取
# 方法一
num = f.read()
count = num.count("itheima")
print(f"次数有{count}")

# 方法三
count = 0
for line in f.readlines(): # 将数据一一传入line中
    line = line.strip().split() # 去掉前后空格以及换行符/n
    # 当后边需要换行符时，一定要再次手动打印出来
    # split 方法是将字符串返回成列表
    for word in line: # 将line中的数据一个个拿出来穿个word
        if word == "itheima":
            count +=1
print(f"{count}次")

# 方法二
for i in f.readlines():
    i = i.strip()
    for word in i.split(" "): # 进行每个单词的切分来判断一行有几个
        if word == "itheima":
            count +=1

# 关闭文件
f.close()

print(f"itheima出现了{count}次")