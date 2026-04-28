# 函数综合案例：黑马ATM
# 本次课题案例使用了函数、if判断结构、while循环结构
# global、continue、break、input语法
# 定义全局变量
money = 5000000
name = None
# 客户姓名
name = input("输入您的姓名：")
# 定义查询余额函数
def query(show_header):
    if show_header:  # 为true则输出表头，反之不行
        print("----------查询余额----------")
    print(f"{name},您好，您的余额剩余{money}")

# 定义存款函数
def saving(num):
    print("----------存款----------")
    global money # global可以对全局变量修改为局部变量
    money += num  # 存入后的余额
    print(f"{name},您好，您的存款金额为{num}")
    query(False) # 调用查询余额函数，False以显示余额，不输出其表头

# 定义取款函数
def goin(num):
    print("----------取款----------")
    global money # global可以对所需要的全局变量修改为局部变量
    money -= num
    print(f"{name},您好，您的取款金额为{num}")
    query(False) # 调用查询余额函数，，False以显示余额，不输出其表头

# 定义主函数
def main():
    print("-----------主菜单-----------")
    print(f"{name},您好。欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额 [输入1]")
    print("存款\t\t[输入2]")  # 通过制表符\t来进行对齐操作
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：") # 直接进行返回输入

# 设置无限循环，确保程序不退出
while True:  # True表示程序可以无限循环，
    keyword_input = main()  # 设置一个变量对主函数进行调用
    if keyword_input == "1":  # 用判断结构来逐次调用其他函数程序
        query(True)
        continue # 跳过本次循环进入下一个循环
    elif keyword_input == "2":
        num = int(input("请输入你要存款的金额："))
        saving(num)
        continue
    elif keyword_input =="3":
        num = int(input("请输入你要取款的金额："))
        goin(num)
        continue
    else:
        print("程序退出")
        break  # 直接对程序进行终止