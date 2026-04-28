# 函数传参练习

def meassage(name ,age ,*args,**kwargs):
    print(f"我叫{name}，今年{age},我的爱好是: ",end='')
    for i in args:
        print(i,end='')

    print()
    print("我的其他信息：")
    for key in kwargs:   # kwargs是字典
        print(f"{key}:{kwargs[key]}",end='')
    print()

meassage("索旭哲",24,"篮球，台球，羽毛球，乒乓球",
         addr = "西安", t_num = 15738320202, money = 1038987)
