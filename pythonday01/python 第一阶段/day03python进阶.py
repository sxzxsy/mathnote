# 函数多返回值
def func():
    return 1,2

x,y=func()  # return将返回值返回给函数调用者func()
print(x,y)

# 函数的多种传参形式
# 位置参数：调用函数时更具函数定义的参数位置来传递参数
def func_x(name ,age ,height):
    print(f"姓名：{name}，年龄：{age},身高{height}")

# 位置调用（位置参数）,要做到实参和形参一一对应
func_x("sxz",25,170)

# 关键字参数：
def func_x(name ,age ,height):
    print(f"姓名：{name}，年龄：{age},身高{height}")

# 位置调用（位置参数）
func_x(name="sxz",age=25,height=170)

# 缺省参数
def func_x(name ,age,height,gender="男"):
    print(f"姓名：{name}，年龄：{age},身高{height},性别{gender}")

# 位置调用（位置参数）
func_x("sxz", 24,170)


# 不定长参数 将传入的数据全部收集到args中
def func_x(name ,*args ):
    # *号表示手机全部参数到元组中
    print(f"姓名：{name}，年龄都有：{args}")
    for i in args:
        print(i)

# 位置调用（位置参数）
func_x("sxz",25,24,23,22,21,20)