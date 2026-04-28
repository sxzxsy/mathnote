# 闭包演示
"""
def 外部函数名(形式参数):
      外部函数的变量

      def 内部函数名(形式参数):
          使用外部函数的变量

      return 内部函数名

调用
内部函数名 = 外部函数名()
内部函数名()

"""

def num(a):

     def add(b):
         x = a+b
         print(x)
     return  add
# 调用
add = num(1)
add(2)

