# 学生类文件
class student():
    # 定义魔法方法，初始化学生的属性
    def __init__(self, name, age, gander, mobile,desc):
        """

        :param name:  学生姓名
        :param age:   学生年龄
        :param gander:  学生性别
        :param mobile:  学生号码
        :param desc: 学生描述信息
        """
        self.name = name
        self.age = age
        self.gander = gander
        self.mobile = mobile
        self.desc = desc

    # 定义魔法方法，输出对象信息
    def __str__(self):
        return \
        f"姓名：{self.name},年龄：{self.age},性别：{self.gander},号码：{self.mobile},描述信息：{self.desc}"


# 测试
if __name__ == '__main__':

    # 实例对象创建
    stu = student("索旭哲",24,'男',"1888888888","千万富翁")
    # 调用
    print(stu)
