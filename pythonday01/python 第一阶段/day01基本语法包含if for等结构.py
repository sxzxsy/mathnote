# python的重新学习之旅
"""
a = "索旭哲"
b = "薛思雨"
result = "我们希望的是: %s 和 %s 永远在一起" %(a,b)
print(result,type(result))
# 类型转换
a1 = float (5)
c =4
print((a1+c) , type(a1))
# 练习
money = 10000000
name = "索旭哲"
salary = 20000
result = money+salary
answer = "我是:%s ,余额:%d ,工资:%d,总计:%d" %(name,money,salary,result)
print(f"我是{name} 我的银行可余额有{money}元"
      f"今天的工资发了{salary},现在我的余额还剩下{result}元")
print(answer)

# 输入
name = str(input("告诉我你是谁？"))
print(name)

# 判断
while (True):
      age = int(input("请输入您的年龄："))
      if age <18:
            print("未成年不得入内")
      else:
            print("祝您玩得愉快！")


# 练习
num = 10
if  int(input("请输入第一次猜测的数字：")) == num:
      print("猜中了")
elif int(input("请输入第二次猜测的数字：")) == num:
      print("第二次中l")
elif int(input("请输入第三次猜测的数字：")) ==num:
      print("第三次中了")
else:
      print("都错了笨蛋")
"""

"""
# 嵌套
print("——————西安市私人相亲会，根据提示输入您的个人信息——————")
age = int(input("输入你的年龄："))
money = int (input("输入您的余额："))
if age >=18:
      print("牛逼。真年轻")
      height = int (input("再输入您的身高："))
      if height >=180:
            print("外形和年龄达标")
      else:
            print("就年龄达标了，可以观察观察")
elif money >1000000:
      print("年轻有为啊")
      car_memary = int(input("输入您的车价："))
      if car_memary >=300000:
            print("卧槽，年龄不达标，但是有存款，还有一个好车")
      else:
            print("滚犊子")
else:
      print("条件不符合")

# 猜数字
import random
num2 = random.randint(1,10)

print("数字猜测游戏，有三次机会，若均为猜错，则您的条件不符")
print("游戏开始")
answer = int(input("第一次猜测数字："))
if answer == num2:
      print("一次就中了")
else:
      if answer>num2:
            print("有点大")
      else:
            print("小了")
      print("第一次结束，开始第二次")
      answer1 = int(input("第二次猜测数字："))
      if answer1 == num2:
            print("第二次中了")
      else:
            if answer1 > num2:
                  print("有点大")
            else:
                  print("小了")
            print("第二次结束，开始第三次")
      answer2 = int(input("第三次猜测数字："))
      if answer2 == num2:
            print("中了")
      else:
            if answer2 > num2:
                  print("有点大")
            else:
                  print("小了")
            print("第三次结束，都猜错了")
"""


# # 循环
# i = 1
# while i<=5:
#       print("我会成为千万富翁")
#       i +=1
# print("35以后会成为的")
#
# j = 1
# while j<5:
#       print(f"今天是第{j}天，准备去表白")
#       y = 1
#       while y<9:
#             print(f"送给你第{y}朵玫瑰花")
#             y +=1
#       print("小雨，我爱你")
#
#       j +=1
# print(f"今天是第{j}天，表白成功")
#
# # 九九乘法表
# i = 1
# while i<=9:
#       j =1
#       while j <=i:
#             print(f"{j}* {i} = {j * i}",end="\t")
#             j +=1
#
#       print()
#       i +=1
#
# print("-----------------------------------------------")
#
# name = "itheima is a brand of itcast"
# count = 0
# for i in name:
#       if i == "i":
#             count +=1
# print(f"{name}中有{count}个i")
#
# print("-----------------------------------------------")
# # 九九乘法表
# for i in range(1,10):
#
#       for j in range(1,10):
#             if j<=i:
#                   print(f"{j}* {i} = {j * i}", end="\t")
#       print()



