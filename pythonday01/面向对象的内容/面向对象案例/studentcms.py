# 管理系统文件
# 需求：
"""
创建学生管理系统
存储数据的形式：列表存储学院对象
显示界面
系统功能
     1.添加学员信息
     2.删除学员信息
     3.修改学员信息
     4.查询学员信息
     5.显示所有学员信息
     6.保存学员信息
     7.退出系统
"""

from student import student # 导包
import time
# 学生管理系统

class studentcms(object):
    # 通过魔法方法init，初始化属性信息
    def __init__(self):
        # 创建一个空列表用于存储学生信息
        self.stu_list = []
    # 定义函数，实现打印管理系统界面
    # 该函数中没有使用self,创建静态方法
    @staticmethod # 静态方法 作用：静态方法不需要实例化对象，可以直接调用
    def show_view():
        print("*" * 25)
        print("学员管理系统v2.0可完成如下操作：")
        print("\t\t1.添加学员")
        print("\t\t2.修改学院")
        print("\t\t3.删除学员")
        print("\t\t4.查询某个学员")
        print("\t\t5.显示所有学员")
        print("\t\t6.保存信息")
        print("\t\t0.退出系统")
        print("*" * 25)

    # 定义函数，实现添加学生信息
    def add_student(self):
        # 输入学生信息
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        gender = input("请输入学生性别：")
        mobile = input("请输入学生手机号：")
        desc = input("请输入学生描述信息：")
        #上述信息封装成学生对象
        stu = student(name,age,gender,mobile,desc)
        # 将学生对象添加到列表中
        self.stu_list.append(stu)
        print(f"添加学生信息成功，信息是：{stu}")


    # 定义函数，实现删除学生信息
    def delet_student(self):
        delet_name = input("请输入要删除的学生姓名：")
        # for循环遍历列表，寻找姓名相同的学生组
        for stu in self.stu_list:
            # 如果信息相同，就进行删除，如果列表不存在数据就先添加
            if stu.name == delet_name:
                self.stu_list.remove(stu)
                print(f"学生{stu.name}信息删除成功")
                break
            else:
                print("没有该学生信息，先加学生信息")
                if len(self.stu_list) == 0:
                    print("列表为空，请添加信息：")
                    self.add_student()

    # 定义函数，实现修改学生信息
    def updat_student(self):
        updat_name = input("请输入要修改的学生姓名：")
        # for循环遍历列表，寻找姓名相同的学生组
        for stu in self.stu_list:
            # 如果信息相同，就进行修改，如果列表不存在数据就无法修改
            if stu.name == updat_name:
                # 提示用户录入新的学生信息
                stu.age = input("请输入修改后的年龄：")
                stu.gender = input("请输入修改后的性别：")
                stu.mobile = input("请输入修改后的电话：")
                stu.desc = input("请输入修改后的描述信息：")
                print(f"修改完成,修改后的信息是姓名{stu.name},年龄{stu.age},性别{stu.gender},手机号{stu.mobile},描述信息{stu.desc}")
                break
            else:
                print("没有该学生信息，修改信息失败")


    # 定义函数，实现查询单个学生信息
    def search_one_student(self):
        # 进行for循环遍历列表，寻找姓名相同
        search_name = input("请输入要查询的学生姓名：")
        # 如果列表中存在数据，就进行for循环遍历
        for stu in self.stu_list:
            # 判断姓名相同，并且列表中该姓名的数量为1，则进行打印
            if stu.name == search_name: #and self.stu_list.count(search_name) == 1:
                print(f"查询成功，信息是：{stu}")
            #     break
            # elif stu.name == search_name and self.stu_list.count(search_name) > 1:
            #     # 如果列表中存在多个姓名相同的数据，则进行打印
            #     print("查询失败，该个人信息在列表中有其相同数据，无法共同展示")
            else:
                print("没有该学生信息，请重新输入")


    # 定义函数，实现查询所有学生信息
    def search_all_student(self):
        # 先判断列表中是否有数据，也就是列表长度为0，则提示用户添加数据
        if len(self.stu_list)==0 :
            print("列表为空，请添加信息：")
            self.add_student()
        else:
         # 如果不为空，通过for循环遍历列表来进行打印
            print("以下是所有学员信息")
            for stu in self.stu_list:
                print(stu)
            print() #换行

    # 定义函数，实现保存学生信息 ,就是将列表类型转为字符串存入文件中
    def save_student(self):
        # 先打开文件
        with open("./stu_data.txt", "w", encoding="utf-8") as f:
            # 把[对象，对象，对象，。。。]转换成[字典，字典，字典]
            stu_list = [stu.__dict__ for stu in self.stu_list] # 列表推导式
            # 再把字典列表，持久化到文件中
            f.write(str(stu_list)) # 转为字符串再写入


    # 实现加载学生信息
    def load_student(self):
        #10.1 加入异常处理
        try:
            #10.2 关联学生信息文件
            with open("./stu_data.txt", "r", encoding="utf-8") as f:
                #一次性读取文件内容
                stu_data = f.read()
                #10.3 读取文件内容，转为列表
                stu_list = eval(stu_data)
                # 判断如果列表为空，就赋予空列表
                if len(stu_list) == 0:
                    self.stu_list = []
                # 把stu_list(列表套字典)转成[学生对象，学生对象...],并赋值给self.stu_list
                self.stu_list = [student(**stu) for stu in stu_list]
        except:
            # 10.4 如果文件不存在，创建一个文件
            with open("./stu_data.txt", "w", encoding="utf-8") as f:
                pass
    # 定义函数，把上边业务全部跑通
    def start(self):
        #11.1 加载学生信息
        self.load_student()
        # 11.2 接送用户内容 ,为了效果更明显，加个时间延迟
        time.sleep(3)
        print(f"欢迎来到学生管理系统")
        #11.3 死循环
        while True:
            # 11.4 打印提示界面
            studentcms.show_view()
            # 11.5 显示用户要操作的编号，并接受
            input_num = input("请输入你要选择的号码：")
            if input_num == "1":
                # 添加学信息
                #print("添加学生信息")
                self.add_student()
            elif input_num == "2":
                # 删除学生信息
                #print("删除学生信息")
                self.delet_student()
            elif input_num == "3":
                # 修改学生信息
                #print("修改学生信息")
                self.updat_student()
            elif input_num == "4":
                # 查询某个学生信息
                #print("查询某个学生信息")
                self.search_one_student()
            elif input_num == "5":
                # 显示所有学生信息
                #print("显示所有学生信息")
                self.search_all_student()
            elif input_num == "6":
                # 保存学生信息
                self.save_student()
                print("保存学生信息成功")
            elif input_num == "0":
                # 退出系统
                result =input("你确定要退出系统吗？y/n")
                if result.lower()== "y": #lower()将大写字母转换成小写
                    # 在推出前进行自动保存信息功能
                    self.save_student()
                    print("已退出系统")
                print("欢迎下次再来")
                break
            else:
                print("输入的编号有误，请重新输入")

# 测试
if __name__ == '__main__':
    cms = studentcms()
    # 启动系统
    cms.start()


