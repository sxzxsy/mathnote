# __init__()
# 每次创建对象的时候自动触发该类的__init__()函数
class stu:
    name = None  # 这些都可以省略
    age = None
    gender= None
    famaliy = None

    # 定义成员方法 ，构造__init__()方法
    def __init__(self,name , age ,gender, famaliy):
        """

        :param name:  学生姓名
        :param age:   学生年龄
        :param gender:  学生性别
        :param famaliy:  学生家庭住址
        """
        self.name = name    # 同时也定义了这四个成员变量
        self.age = age      # 在类创建中，也就不需要再次进行成员变量的定义
        self.gender = gender
        self.famaliy = famaliy

# 创建对象，自动为属性赋值
stu_01 = stu("索旭哲",22,'男',"陕西")

print(stu_01.name)
print(stu_01.age)
print(stu_01.gender)
print(stu_01.famaliy)




# __str__()
# 当使用print输出对象时，默认打印对象的内存地址，
# 一般情况下都会重写，改为打印对象的各个属性值。
# ## Print（对象）输出语句打印对象，默认调用了该对象 所在类 的str魔法方法
class car:

    # init方法
    def __init__(self,color,num):
        self.color =color
        self.num = num

    # str方法

    def __str__(self):
        return f"颜色{self.color},轮胎数{self.num}"

# 创建对象
c = car("绿色",9)

# 当Print（对象）输出语句打印的是对象时，默认调用了该对象 所在类 的str魔法方法
print(c)
# 当输出语句正常做输出时，不做任何调用
print(f"颜色{c.color},轮胎数{c.num}")



# __del__()
# 当删除对象时,(调用del删除对象或文件执行结束后)python解释器会默认调用__del__()方法
# 当.py文件执行结束时，或者手动进行del释放对象资源，会自动调用该函数
# 当手动调用时执行在程序之前，反之，自动调用时执行在程序结束以后
# 定义一个汽车品牌类型
class car1:
    # 构造init方法
    def __init__(self,brand):
        """

        :param brand:  汽车品牌
        """
        self.brand = brand

    # 构造str方法 打印对象属性值，可以免去手动打印对象中的属性值
    def __str__(self):
        return f"品牌：{self.brand}"

    # 构造del方法 删除对象时，给出提示
    def __del__(self):
        print(f"{self},对象被删除了")

# 创建对象
c = car1('斯巴鲁BRZ_2026款')
# 有str,所以调用对象时，默认调用该对象所在类的str方法
print(c)
# 手动访问brand
print(c.brand)

print("程序结束了！")

