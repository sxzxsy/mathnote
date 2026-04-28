# 普通的对象中，参数赋值太过于繁琐
# 引入__init__()方法，可以节省书写重复代码的工作
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


stu_01 = stu("索旭哲",22,'男',"陕西")

print(stu_01.name)
print(stu_01.age)
print(stu_01.gender)
print(stu_01.famaliy)