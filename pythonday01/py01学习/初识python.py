# name="hello word"
# print(name)
# # 总额50元，买了冰淇淋10元，还剩多少元
# moeny = 50  # 总余额50
# moeny = moeny-10
# moeny = moeny-5
# print(f"余额还剩：{moeny}")
#
# #将数字类型/浮点数类型转换为字符串
# num_str = str(11)
# print(num_str,type(num_str))
#
# float_str = str(11.234)
# print(float_str,type(float_str))
#
# # 将字符串转换为数字
# str_num = int('11')
# print(str_num,type(str_num))
#
# # 整数转换浮点数
# num_1 =float(11)
# print(num_1,type(num_1))
# # 浮点数转换为整数
# num_float = int(11.2345)
# print(num_float,type(num_float))
#
# # 算术运算符练习 +,-,*,/,//(整除),%(取余),**(求方)
# a = 1
# b = 2
# c = a+b
# d=c-a+b
# print(int(d))
#
# # 赋值运算符 +=，-=，/=，*=，//=，**=
# c = 1
# b = 2
# a = 3
# c += a  # 相当于c + a =c
# b -= c  # 相当于b - c = b
# print("c +=a:",c)
#
# # 字符串
# name = "楼的华"
# age = "54"
# print(f"我的名字是：{name}，今年{age}岁")
#
# name = "黑马"
# message = "学习IT就来 %s" % name  # %表示：我要占位 s表示：将变量变成字符串放入占位的地方
# print(message) # %d 将内容转换成整数  %f 将内容转换成浮点数
#
# name = "英雄联盟"
# age = 2004
# stock_price = 19.89 # m控制输出值宽度，.n控制小数点精度
# message = "%s,成立于：%d,今天的股价是：%5.2f" %(name,age,stock_price)
# print(message)
#
#
# # 练习：完成下列练习
# name = "百度"
# stock_price = 34.98  # 股价
# stock_code = "12334554" # 股票代码
# stock_price_daily_growth_factor = 1.2 # 股票每日增长系数
# growth_days = 10 # 增长天数
# # stock_price_daily_growth_factor ** growth_days 十天后的增长系数
# finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days # 十天后的股价
# print(f"公司{name}，股票代码：{stock_code},当前股价{stock_price}")
# print("每日增长系数%1.1f,经过%d天增长后当前股价为%2.2f" %(stock_price_daily_growth_factor,growth_days,finally_stock_price))
#
#
#
# # input()输入语句 默认输入字符串类型数据
# print("请告诉我你是谁：")
# name = input()
# print(f"你是{name}") # print("你是：%s" % name)
# name = input("请告诉我你是谁：")
# print("你是:%s" % name)
#
# # 输入整数 输入转换为Int类型
# num = int(input("请输入你的银行卡密码："))
# print(f"密码：{num},输入成功。",type(num))
#
# ### 练习习题
# user_name = input("请输入您的姓名")
# user_type = input("请输入您的等级")
# print(f"您好，{user_name},您是尊贵的的{user_type}用户，欢迎光临")
#

# # ###第三章节 Python判断语句
# # 布尔类型  True 为真  False 为假
# result = 10>5  # 其他符号 == ,!= ,> ,< ,>= ,<=
# print(f"10>5的结果是{result}" , type(result))
#
# # if判断语句
# # if 要判断的条件：
# #     条件成立时,要做的事情
# age = int(input("请输入你的年龄"))
# if age >= 18:
#     print("我已经成年了")
# else:
#     print("那好吧，我还差几岁")

# # ## 课后练习
# print("欢迎来到星星网咖！")
# age =  int(input("请告知你的年龄："))
# if age >= 18:
#     print("你已成年，祝您用网愉快")
# else:
#     print("不好意思，未成年不得进入")
# print("欢迎下次再来！！！")
#
# #练习
# print("欢迎来到游乐园")
# user_height = int (input("请输入你的身高(cm)："))
# if user_height >= 120:
#     print("您的身高超过120cm，游玩需要10元加购")
# else:
#     print("您的身高未超过120cm可以免费游玩")
#
# print("祝您玩得愉快的！")

# # if elif else语句 判断为互斥且有顺序的，满足1 将不会关注后边的语句，同理满足2 亦是如此
# num = int(input("请输入你的数字"))
# num_1 = int(input("输入你的长度"))
# if num >18:
#     print("牛逼")
# elif 11<num_1<16:
#     print("垃圾")
# else:
#     print("算了你回家吧")
#
# print("结束了")
#
# # 练习2
# if int(input("请输入你的年龄：")) >18:
#     print("年龄大于18，免费")
# elif int(input("请输入你的vip等级"))>3:
#     print("等级大于3，可以免费玩")
# elif int(input("今天几号：")) ==1:
#     print("刚好是一号，今天免费")
# else:
#     print("不好意思条件都不满足")

# # #3练习三
# num = 10
# if int(input("请输入第一次猜想的数字：")) ==num:
#     print("恭喜你，第一次就对了")
# elif int(input("不对，再猜一下：")) == num:
#     print("恭喜你，第二次猜对了")
# elif int(input("不对，再来最后一次：")) ==num:
#     print("终于猜对了！")
# else:
#     print(f"都猜错了，结果是{num}")
#


# # # ##判断语句的嵌套使用 使用if elif else进行嵌套
# num = int(input("输入数字："))
# if num >=5:
#     print("数字达标")
#     age =int(input("输入年龄："))
#     if age >=18:
#         print("你已经成年，有权利去做")
#         year = int (input("输入年限"))
#         leval = int(input("输入级别："))
#         if year>3:
#             print("年龄和年限都达标")
#         elif leval >3:
#             print("年龄和级别达标，可以领取")
#         print("所有条件都满足，可以领取")
#     else:
#         print("未成年不好意思")
# else:
#     print("数字不达标")
#     hegiht = int(input("输入你的身高："))
#     if hegiht >= 170:
#         print("你的身高达标，可以免费")
#     else:
#         print("年龄不合适，不好意思")
# print()


# 使用之前所学习过的知识进行案例练习
# 案例： 定义一个数字（1——10，随机产生），通过三次机会进行判断
# 随机产生数字的语法： random。randint(m , n)
# import random
# num = random.randint(1 ,10)
# num_1 = int(input("请输入猜测的数字："))
# if num_1 == num:
#     print(f"恭喜你，一次就猜测成功了，结果为{num}")
# else:
#     print("不好意思，你猜错了")
#     if num_1 > num:
#         print("猜大了")
#     else:
#         print("猜小了")
#     num_2 = int(input("请再次输入："))
#     if num_2 == num:
#         print(f"恭喜你，第二次才对了{num}")
#     else:
#         print("不好意思，你又猜错了")
#         if num_2 > num:
#             print("猜大了")
#         else:
#             print("猜小了")
#         num_3 = int(input("请再次输入："))
#         if num_3 == num:
#             print(f"恭喜你，第三次才对了{num}")
#         else:
#             print("不好意思，都猜错l,三次机会使用完了")
#             if num_3 > num:
#                 print("猜大了")
#             else:
#                 print("猜小了")
# print()


# #####第四章 循环语句之“while”语句##########
# #####第四章 循环语句之“while”语句##########
# #####第四章 循环语句之“while”语句##########

# i = 0 说出99次,小美,我喜欢你
# while i < 100:
#     print("小美，我喜欢你")
#     i += 1
# print("成功")

# 案例练习 求 1-100的和
# sum = 0 # 定义变量，对每次循环后的数字进行累加
# i = 1
# while i < 101:
#     sum += i
#     i +=1
# print(f"1-100的和的结果={sum}")

# while 循环的基础案例   定义随机数进行猜测
# import  random
# num = random.randint(1,10) # 定义1-100的随机数
# sum = 0
# flag = True  # 循环条件
# while flag:  # 保持无限循环
#     num_1 = int(input("输入猜测的数字："))
#     if num_1 == num:
#         print("猜中了")
#         flag = False
#     else:
#         print("猜错了")
#         if num_1 < num:
#             print("猜小了")
#         else:
#             print("猜大了")
#     sum +=1
#     print(f"猜了{sum}次")


# while循环语句的嵌套使用
# 案例练习，表白一百天，每天都送十朵玫瑰
# i = 1  # 定义一个变量为天数,从第一天开始
# # 外层循环控制天数
# while i <=100:
#     print(f"今天是第{i}天，准备表白")
#     j = 1 # 定义一个变量为玫瑰花数
#     # 内层循环控制玫瑰花数
#     while j <=10:
#         print(f"送给小美第{j}朵玫瑰花")
#         j +=1
#     print("小美。我喜欢你")
#     i +=1
#
# print(f"坚持到{i-1}天，表白成功")



# print 会自动换行,可以使用print("" , end = '')进行输出不换行的功能
# 使用\t 可以进行对齐 print("a\t b")

# 案例练习 使用循环语句完成九九乘法表
# 使用一个i循环来控制行
# 使用一个j循环来控制列的
# i = 1 # 变量i控制行
# while i<=9:
#
#     j = 1 # 变量j控制列
#     while j <=i:  # 列受行的影响,逐渐递增
#         print(f"{j}*{i}={j * i}\t", end='') # 使用制表符\t进行对齐和end = ''来不变行
#         j +=1
#
#     i +=1
#     print() # Print输出内容,表示对每次循环结束后的结果值进行换行
#

# #####for循环的基础语法######
# while循环的循环条件是自定义的,自行控制循环条件
# for循环的是一种"轮询"机制,是对一批内容进行"逐个处理"
# for循环就是将内容,挨个取出

# num = "itheima"
# for a in num:
#     # 将num中的内容,挨个取出赋予a临时变量
#     # 就可以在循环体内对a进行处理
#     print(f"输出:{a}")
#
# # 案例练习
# # 统计有多少个a
# name = "itheima is a brand of itcast"
# sum = 0
# for  x in name:
#     if x == "a":
#         sum +=1
# print(f"有{sum}个a")


# range语句
# range(num) 获取一个从0开始到num结束的数字序列,不包含num本身
# range(num1,num2) 获取一个从num1开始到num2的数字序列,不包含num2
# range(num1,num2,step)获取一个从num1开始到num2的数字序列,不包含num2,step是数字之间的步长数值
# for x in range(10):
#     print(x)
#
# for  x in range (1,10,2):
#     print(x)
#
# # 案例练习
# for x in range(10):
#     print(f"总共送了{x}朵玫瑰花")
#
# # 案例练习  请算出1-101中总共有多少个偶数
# sum = 0
# num =101
# for x in range(1,num):
#     if x % 2 == 0:
#         sum +=1
# print(f"有{sum}个偶数")

# for循环的嵌套使用
# 坚持表白100天
# 每天送花100束
# i = 1
# for i in range(1,101):
#     print(f"今天是表白的第{i}天")
#     j = 0
#     for j in range(1,11):
#         print(f"送给小美第{j}朵花")
#     print(f"小美,我喜欢你(第{i}天表白结束)")
#
# print(f"表白{i}天,表白成功")
# ## for 与 while共同使用
# i = 1
# for i in range(1,101):
#     print(f"今天是表白的第{i}天")
#     j = 1
#     while j <=10:
#         print(f"送给小美第{j}朵花")
#         j +=1
#     print(f"小美,我喜欢你(第{i}天表白结束)")
#
# print(f"表白{i}天,表白成功")
#
#
# # 九九乘法表 用for 循环练习
# for i in range(1,10):  # i定义行数
#
#     for j in range(1,i+1):  # j 定义列数,用i+1来控制他的范围
#         # 第一行有1组数字,第二行2组,一次类推,第九行有九组
#         # 所以j控制每列输出几组数字的范围取决与行数为几,
#         #同理,在range语句规范中 范围只能是"行数+1"
#         print(f"{j}*{i}={j*i}\t",end='') # 使用换行符和对齐符号输出
#     # 外层循环可以通过print输出一个回车符
#     print()
#
# a = 1
# while a <=9: # 控制九九乘法表的行
#
#     b =1
#     while b <=a: # 控制九九乘法比表的列
#         print(f"{b}*{a} ={b*a}\t",end='')
#         b +=1
#     a +=1
#     print()


# #####continue 和 break
# continue: 中断本次循环,直接进入下一次循环
# for i in range(1,5):
#     print("语句1")
#     continue
#     print("语句2")
#
# # break:直接结束循环
# for i in range(1,5):
#     print("语句1")
#     for j in range(1,5):
#         print("语句2")
#         break
#         print("语句3")
#     print("语句4")

# ##########练习案例 :发工资 #############
# ##########练习案例 :发工资 #############
# ##########练习案例 :发工资 #############
# ##########练习案例 :发工资 #############

"""某公司账户余额有10000元,给20名员工发工资
 1:员工编号从1-20 ,从编号1开始,依次领取工资,每人可以领1000元
 2:领工资时,财务判断员工的绩效分数(1-10)(随机生成)
 低于5,不发工资,直接下一位
 3:如果工资发完了,结束发工资"""
money = 10000
for i in range(1,21):
    import random  # 随机数语法
    care = random.randint(1, 10)
    # 判断绩效分
    if care < 5:
        print(f"员工{i},绩效分{care},低于5,不发工资,下一位")
        continue  # 当满足contiue时,直接后边语句不执行,再次循环
    # 判断余额
    if money >= 1000:
        money -=1000
        print(f"员工{i},发放工资1000元,账户余额还剩{money}")
    else:
        print(f"没钱了,不发了,余额{money}")
        break
print()

