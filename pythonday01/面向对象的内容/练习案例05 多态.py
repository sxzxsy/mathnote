# 多态基础演示
class animal:
    def speak(self):
        pass

# 定义子类
class dag(animal):
    # 方法重写
    def speak(self):
        print("狗叫：汪汪汪")

# 定义子类
class cat(animal):
    # 方法重写
    def speak(self):
        print("猫叫：喵喵喵")

# 定义函数接收
def make_noise(a:animal): # 父类调用字类对象
    # 接收对象调用其speak函数
    a.speak()


# 测试
if __name__ == '__main__':

    # 创建对象
    c = cat()
    d =dag()

    # 多态演示
    make_noise(c)
    make_noise(d)