# class 类名（）：
# class 类名（父类）：

# 继承
class father:

    def __init__(self):
        self.gnder = ('男')

    def work(self):
        print("散步")

# 字类继承父类
class son(father):
    pass
#测试子类的功能
s = son()
print(f"性别:{s.gnder}") # 字类从父类继承过来
s.work()


# 摊煎饼
class boss:
    # 定义属性
    def __init__(self):
        self.name = "古法配方"
    # 定义行为
    def jishu(self):
        print(f"采用{self.name}摊煎饼果子")


# 定义徒弟类
class tudi(boss):
    pass

#测试字类功能
t = tudi()
t.jishu()

