#
def func02():
    print("这是func02的开始")
    1/0
    print("结束")

def func01():
    print("这是func01的开始")
    func02()
    print("结束")

def main():
    try:
        func01()
    except Exception as e:
        print("有异：" ,e)

main()