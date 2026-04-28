"""
该文件作为系统入口文件
"""
# 引入学生管理系统文件
from studentcms import studentcms

# 测试
if __name__ == '__main__':
    # 创建管理系统对象
    stu_cms = studentcms()

    # 启动系统
    stu_cms.start()