# 函数
def name():
      print("你好")
name()

def hegiht (num):
      print(f"您的身高是{num}")
hegiht(20)

# 函数调用，无返回值
def add(x,y):
      result = x + y
      print(f"结果是{result}")

add(1,2)

# 返回值 举例
def add(a,b):
      result = a + b
      return result
r = add(1,2)
print(f"结果是{r}")

# 函数调用
def fun_c():
      print("--2--")

def fun_d():
      print("--1--")
      fun_c()
      print("--3--")

fun_d()



# 函数作为参数传递
# 形式参数，可以接受函数传入
# 实际参数，真的可以传入一个参数
def num(num1):  # num1函数作为参数传入
    result = num1(1,2)   # num1函数拿进来以后，进行调用
    print(f"结果是{result}")

def num1(x,y): # 加法运算
   return  x+y

num(num1) # 调用num函数，并将num1函数作为参数拿到num中去


# 匿名函数
def num (a):
    result = a(1,2)
    print({result})

num(lambda x,y :x+y) # 调用函数 匿名函数作为参数传入


