# 国家部门制定了打印机标准
# 创建一个打印抽象类
# ABC是 Abstract Base Class 抽象基类
# 它的作用是用来什么一个类是抽象类
from abc import  ABC ,abstractmethod
class printer(ABC):
    @abstractmethod
    def  Black_and_white(self):  # 黑白打印
        pass
    @abstractmethod
    def Color(self): # 彩色打印
        pass  #

# 硬件入围
class hp(printer):
    def Black_and_white(self):
        print("HP打印机打印黑白")
    def Color(self):
        print("HP打印机打印彩色")

class xiaomi(printer):
    def Black_and_white(self):
        print("小米打印机打印黑白")
    def Color(self):
        print("小米打印机打印彩色")
class conon(printer):
    def Black_and_white(self):
        print("佳能打印机打印黑白")
    def Color(self):
        print("佳能打印机打印彩色")


# 入围测试平台
def make_test(printer):
    print("=" * 20)
    print("开始测试打印机")
    printer.Black_and_white()
    printer.Color()
    print("测试结束")
    print("="*20)


# 测试
if __name__ == "__main__":
    # 创建对象
    hp1 = hp() # 创建hp对象
    xiaomi1 = xiaomi() #
    conon1 = conon() #
    # 调用测试方法
    make_test(hp1)
    make_test(xiaomi1)
    make_test(conon1)
