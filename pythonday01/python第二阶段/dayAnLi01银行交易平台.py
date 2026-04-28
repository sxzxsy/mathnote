# 银行存取款ATM机效果展示
print("---------交通银行信息交易平台---------")
money = int(input("请输入您的余额："))
name = str(input("请输入您的姓名："))


# 主菜单展示
def main():
    print("---------主菜单---------")
    print(f"尊敬{name}先生/女士您好，欢迎来到交通银行ATM交易平台，请您根据一下选项进行选择")
    print("查询余额[输入1]")
    print("进行存款[输入2]")
    print("进行取款[输入3]")
    print("退出页面[输入4]")
    intput_choose = int(input("请输入您的选择："))
    return intput_choose

#查询余额效果
def query(head):
    if head ==True:
        print("---------查询余额---------")
    print(f"{name}先生/女士您好，您的账户余额为{money}")


#进行存款效果函数
def saving(num):
    print("---------进行存款---------")
    global money
    money += num
    print(f"{name}您好，您存款{num}成功")
    query(False)

def goin(num):
    print("---------进行取款---------")
    global money
    money -= num
    print(f"{name}您好，您取款{num}成功")
    query(False)


# 设置无限循环来确保程序持续进行
while True:
    keyword_input = main()  # 调用函数
    if keyword_input == 1:  # 进行数值对比来确认选项
        query(True)
        continue
    elif keyword_input==2:
        num = int(input("输入您要存款的金额："))
        saving(num)
        continue
    elif keyword_input==3:
        num = int(input("输入您要取款的金额："))
        goin(num)
        continue
    else:
        print("程序退出，欢迎下次光临")
        break






