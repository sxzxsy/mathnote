# 抽象类（接口的演示）
# 冰箱的规格，以及各大厂商的操作流程
# 定义抽象类 （冰箱规格）
class bx:
    # 必须能制热
    def hot(self):
        # 制热
        pass

    # 必须能制热
    def cool(self):
    # 制冷
        pass

    # 必须能左右摆风
    def swing(self):
        #白凤
        pass

# 美的类
class medi(bx):  # 有继承
    # 制热功能
    def medi_hot(self):  # 有重写
        print("美的先进电丝通电制热技术")
    def medi_cool(self):
        print("美的核心液氮制冷技术制冷")
    def medi_swing(self):
        print("美的无声叶片摆风技术")

# 小米类
class xiaomi(bx):
    # 制热功能
    def xiaomi_hot(self):
        print("小米先进电丝通电制热技术")
    def xiaomi_cool(self):
        print("小米核心液氮制冷技术制冷")
    def xiaomi_swing(self):
        print("小米无声叶片摆风技术")

# 测试
if __name__ == '__main__':

    # 创建对象
    md = medi()
    xm = xiaomi()

    # 多态展示 方法调用
    md.medi_swing()
