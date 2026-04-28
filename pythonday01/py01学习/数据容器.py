# # 数据容器
# # List
# # 通过下标索引取值
# a_list = ["we","me",["you",0]]
# print(a_list[2][1])
# print(a_list[-1])  # 倒序取出所需元素
# print(a_list[-3])
#
# # 查询某元素的下标
# # 语法：列表.index(元素)
# my_list = ["s","x","z"]
# a = my_list.index("s")
# print(f"下标索引值为：{a}")
# # 修改特定位置（索引）的元素值：
# # 语法：列表[下标]=值
# my_list = ["s","x","z"]
# my_list[1] = "love"
# print(my_list)
#
# # 元素插入
# # 语法：列表.insert(下标，元素)
# my_list = ["s","x","z"]
# my_list.insert(0,"xsy")
# print(f"添加后的值{my_list}")
#
# # 列表尾部追加"单个"新元素
# # 语法：列表.append(元素)
# my_list.append("sxzandxsy yyzyq")
# print(my_list)
#
# # 列表尾部追加"一批"新元素
# # 语法：列表.extend(其他数据容器)
# my_list1 = ["love","forever"]
# my_list.extend(my_list1)
# print(my_list)
#
# # 删除元素
# # 语法1：del.列表[下标]
# # 语法2：列表.pop(下标)
#
# # 删除某元素在列表中的第一个匹配项（相同项）
# # 语法：列表.remove(元素)
#
#
# # 清空列表
# # 语法：列表.clear()
#
#
# #统计列表内某元素的数量
# # 语法：列表.count(元素)
#
#
# # 统计列表中全部的元素数量
# # 语法：len(列表)
#
# # 案例练习
#
# me_list =[21,25,21,23,22,20]
# # 追加一个数字31，到列表的尾部
# me_list.append(31)
# print(me_list)
# # 追加一个新列表到列表尾部
# me_list1 =[29,33,30]
# me_list.extend(me_list1)
# print(me_list)
# # 取出第一个元素
# a = me_list[0]
# print(f"结果是{a}")
# # 取出最后一个元素
# a1 = me_list[-1]
# print(f"结果{a1}")
# # 查找元素31，在列表中的下标位置
# b = me_list.index(31)
# print(f"位置{b}")

# # 列表的遍历，分别是while和for循环
# def me_list_while():
#     me_list =[21,25,21,23,22,20]
#     index = 0   #定义初始值为0
#     while index<len(me_list):  # 进行判断
#         a = me_list[index]  #采用通过下标索引值来取出元素的方法
#         print(f"结果{a}")
#         index +=1  # 每次循环下标索引值都+1
# me_list_while()
#
# print("wwwwwww")
# def me_list_for():
#     me_list = [21, 25, 21, 23, 22, 20]
#     for i in me_list:
#         print(f"结果{i}")
# me_list_for()
#
#
#
# # #############案例
m_list = [1,2,3,4,5,6,7,8,9,10]
# m_list1 = []
# # 取出偶数，存入新的列表中
# index = 0
# while index < len(m_list):
#     a = m_list[index]
#     if a % 2 == 0:
#         m_list1.append(a)
#     index +=1
# print(m_list1)
#
# print("1111111111111111111")
# # for
# m_list1 = []
# for b in m_list:
#     if b % 2 ==0:
#         m_list1.append(b)
#
# print(m_list1)





# # 元组
# # 无法修改,只能修改内容里边包含列表的元素
my_tuple = (0,"sxz",000)
# print(f"类型是:{type(my_tuple)},内容是{my_tuple}")
# 元组的操作有下标index索引查询，count统计方法，len函数统计元组元素数量
# 使用while和for循环取出元组元素
### while
# index = 0
# t1 = (1,2,3,4,'d',7)
# while index < len(t1):
#     print(f"元素是{t1[index]}")
#     index +=1
#
# # for
# for element in t1:
#     print(f"2元素是：{element}")
#
# # 练习案例
# t_tuple = ("周杰伦",11,["football","music"])
# # 查询年龄所在的下标位置
# a = t_tuple.index(11)
# print(f"位置是{a}")
#
# # 查询学生的姓名
# b = t_tuple[0]
# print(f"姓名是{b}")
#
# # 删除学生爱好中的football
# t_tuple = ("周杰伦",11,["football","music"])
# del t_tuple[2][0]
# print(t_tuple)
#
# # 增加爱好：coding到爱好List中
# t_tuple[2].append("coding")
# print(t_tuple)





# # #######字符串str
# # 字符串中的下标索引是通过字符来锁定，而非每个整体的单词
# # 无法修改
my_str = "sxz love xsy fovever"
# # 字符串的替换
# # 语法：字符串.replace(字符串1，字符串2)
# # 功能：是将字符串内全部的字符串1，替换为字符串2，不是修改，而是得到一个全新的
# new_my_str = my_str.replace("sxz","xsy")
# print(new_my_str)
#
# # 字符串的分割
# # 语法：字符串.split(分隔符字符串)
# # 功能：按照指定的分隔字符串，将字符串划分为多个字符串，并存入列表对象中
# new_my_str = my_str.split(" ")
# print(new_my_str)

# 字符串规整操作
# 语法：字符串.strip()  不传入参数，就是去除首尾空格

# 统计字符串中某字符串出现的次数
# 语法：字符串.count()

# 统计字符串的长度
# 语法： len()

# 序列
# 语法：序列[起始下标：结束下标：步长]




# 数据容器 集和set  特点：不允许重复，不支持下标索引访问，允许修改
my_set = {"黑马", "sxz" ,134 , "and"}
# 添加新元素  集和.add()
# 移除元素   集和.remove()
# 随机取出一个元素   集和.pop()
# 清空集合   集和.clear()
# 取两个集和的差集  集和1.difference(集和2)
# 消除两个集和的差集  集和1.difference_update(集和2)
# 2个集和合并为一个集和  集和1.union(集和2)
# 统计集和元素数量 len(集和)
# 集和的遍历while循环无法遍历，因为集和不支持下标  for




# 字典 包含key Value 存储的都是键值对
# {key:value ,key:value }
meassge_dict = {"sxz" : 24,"xsy":21}
# 不可以使用下标索引，可以通过Key获取到对应的Value
# 语法：字典[Key]
# 定义一个嵌套字典
stu_score_dict = {
    "sxz":{"语文":88 , "数学":88, "英语":100},
    "xsy":{"语文":88 , "数学":88, "英语":100}
}
# 获取一个同学的信息
scor = stu_score_dict["sxz"]["语文"]
print(f"sxz信息是{scor}")

# 新增/更新元素
# 语法:字典[Key] = Value/字典
# 删除元素 字典.pop[Key] = value
# 清空元素  字典.clear()
# 获取全部的Key   字典.keys()
# 遍历字典  用for循环遍历
# 统计字典的元素数量 len(字典)

# 案例

my_dict = {
    "sxz":{"成绩":100 , "身高":172 , "工资":23000,"级别":2},
    "xsy":{"成绩":100 , "身高":164 , "工资":8000,"级别":1},
    "周杰伦":{"成绩":100 , "身高":177 , "工资":230000000,"级别":13},
    "张学友":{"成绩":100 , "身高":182 , "工资":120000000,"级别":11}
}
print(f"升职加薪钱的结果{my_dict}","\t")
# 用for循环遍历字典:
for name in my_dict:
    if my_dict[name]["级别"]<= 1:
    # 进行升职加薪
        # 获取到员工的信息字典
        ifm_my_dict = my_dict[name]
        # 然后修改员工的信息
        ifm_my_dict[name]["级别"] =2 # 级别+1
        ifm_my_dict[name]["工资"] += 10000  # 工资加10000
        # 然后更新回字典
        my_dict[name] = ifm_my_dict
# 输出结果
print(f"升职加薪后结果为{my_dict}")

# 快捷键：shift+alt+鼠标移动

# ########数据容器的通用操作
# 通用排序功能 语法： sorted(容器  , [reverse =True]# 反向排序，也可省略)
# 排序的结果都会变成列表
# 字符串大小比较根据ASCLL码表来进行比较
