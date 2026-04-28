# 要返回多个返回值时，用逗号隔开需要返回的返回值
# 并用多个变量接收即可
def tset_return():
    return  1 , 2 ,3

x,y,z = tset_return()  # 使用多个变量接受即可
print(x)
print(y)
print(z)

# 掌握位置参数:调用函数时根据函数的参数位置来传递参数
def ifo_my(name , age ,score):
    print(f"您的名字{name},年龄{age},成绩{score}")
    # 传递参数和定义的参数的顺序必须一致
ifo_my("索旭哲"  , 24 , 100)


# 掌握关键字参数
def ifo_my(name , age ,score):
    print(f"您的名字{name},年龄{age},成绩{score}")
    # 传递参数和定义的参数的顺序不用一致
ifo_my(name = "索旭哲" ,age =  24 , score = 100)


# 掌握不定长参数  可变参数
# 分为位置传递不定长
# 会根据传进参数的位置合并为一个元组
# 关键字传递不定长
def ifo_my(*name):  # 可以接受无限个参数数量
    print(name)
    # 传递参数和定义的参数的顺序必须一致
ifo_my("索旭哲")
ifo_my("索旭哲" ,18)
# 会组成字典  使用键值对形式接受
def ifo_my(**name):  # 可以接受无限个参数数量
    print(name)

ifo_my(name="索旭哲"  , age = 24 , score = 100)


# 掌握缺省参数
def ifo_my(name , age ,score = 100):
    print(f"您的名字{name},年龄{age},成绩{score}")
    # 传递参数和定义的参数的顺序必须一致
ifo_my(name="索旭哲"  , age= 20,)


# 匿名函数
# 掌握将函数作为参数 传递（在函数内部调用其他函数）


# 定义一个函数，接受另一个函数作为参数
def jisuan_func(computer):  # 是计算逻辑的传入，不是数据的传入！！！！
    result = computer(1,2) # 函数调用
    print(f"结果是{result}")

# 定义一个函数，准备作为参数传入
def computer(x,y):
    return x+y

jisuan_func(computer)

# lambda匿名函数



