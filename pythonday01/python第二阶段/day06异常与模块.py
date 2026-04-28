# # 抓捕常规异常
# 语法：
try:
    """可能发生错误的代码"""
except:
    """如果出现异常执行的代码"""

# # 抓捕指定异常
try:
    """可能发生错误的代码"""
    # print(name)
except "错误类型" as e: # e代表异常的对象
    """如果出现异常执行的代码"""

# # 捕获多个异常 ，但无法区分
"""try:
#     # 可能发生错误的代码
#     print(name)
# except ("错误类型1","错误类型2") as "变量":
#     # 如果出现异常执行的代码
"""
#  捕获所有异常
try:
    print(name)
except Exception as e:
    print("出现异常了")

    
# # 捕获多个异常 ，同时进行区分
# try:
#    # 可能发生错误的代码
#    print(name)
# except ("错误类型1") as "变量":
#     print("文件没找到", "变量")
# except ("错误类型2") as "变量":
#     print("其他原因", "变量")
#     # 如果出现异常执行的代码


# ***** 也就是捕获所有异常
# 不关心什么异常，有问题就进行捕获
try:
    open("asd","r")
except Exception as e: # 变量e来接受Bug
    print(f"出问题了，问题是{e}")




