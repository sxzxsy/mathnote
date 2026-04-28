# 设计一个类
class student:
    # 定义成员变量
    name = None
    age = None
    gender = None
# 基于类创建对象
sut_01  = student()

# 为对象中的的属性进行赋值

sut_01.name = "索旭哲"
sut_01.age = 24
sut_01.gender = "男"
 
# 获取对象中的信息
print(f"信息是{sut_01.name}")
print(f"信息是{sut_01.age}")
print(f"信息是{sut_01.gender}")

# 定义一个带有成员方法的类
class stu:
    name = None
    # 定义一个成员方法
    def massage(self,msg):
        print(f"大家好，我是{self.name},{msg}")

# 创建对象
s = stu()
# 为对象中的属性赋值
s.name = "sxz"
# 成员方法的调用  对象名.方法名（）
s.massage("很高兴和大家成为朋友")