#  python 的函数####
# 函数就相当于一个包装盒,将你需要的东西放在其中,使其可以反复使用
str1 ="sxscc"
str2 = "scvfvf"
str3 = "scsc"
def my_len(data):  # 定义一个函数
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

my_len(str1) # 调用函数 让定义的函数开始工作
my_len(str2)
my_len(str3)

# 函数结构
"""def 函数名(传入参数):
       函数体
       return 返回值"""
# 参数不需要，可以省略
# 返回值不需要，可以省略
def my_name():
    print("sxz")

my_name()

# 练习
def my_card():
    print("欢迎来到黑马\n请出示你的72小时核酸")

my_card()

# 计算任意两个数字之和
def my_add(a,b): # 定义函数
    result = a + b
    print(f"a+b的和是{result}")
my_add(23,46)  #调用函数

