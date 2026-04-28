# 综合训练
class person:

    count = 0 # 记录创建对象数

    def __init__(self,name,age):
        self.name = name
        self.age = age
        person.count += 1 # 每当创建一个对象时，对象数加1

    def __del__(self):
        person.count -= 1  # 每当创建一个对象时，对象数加1
    def show(self):
        print(f"当前对象个数{person.count}")

    # 定义一个show_info方法 输出这是一个person类
    def show_info(self):
        print("这是一个person类")

    # 打印对象是可以打印对象的属性值
    def __str__(self):
        return f"姓名：{self.name},年龄：{self.age}"

    # 定义一个方法study 输出我要好好学习
    def study(self):
        print("我要好好学习")
# 测试
if __name__ == "__main__":
    d1 = person("索旭哲",24)
    d1.show()
    d1.show_info()
    print(d1)

    d2 = person("索旭",23)
    d2.show()




