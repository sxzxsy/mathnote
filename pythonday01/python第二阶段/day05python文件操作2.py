# 文件操作的三大步骤
# 文件打开  不推荐
fl = open("文件名" ,"读或者写" ,encoding="utf-8")

# 文件读/写
for i in fl:
    print(i.strip())  # 自行处理\n
# 文件关闭
fl.close()

# 方式2
for i in open("文件名" ,"读或者写" ,encoding="utf-8"):
    print(i.strip())

fl.close()

# with open语法  不推荐
with open("文件名" ,"读或者写" ,encoding="utf-8") as f:
    for line in f:
        print(line.strip())
# 不需要写close
# 在python中任何with xxx as xx： 的写法，都可以做到不用写close




