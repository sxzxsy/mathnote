# 烤地瓜
#2.属性：被烤时间cook_time,烘培状态cook_state,调料coniments
#3.行为:烘烤cook（）。添加调料add_coniments
#4.魔法方法：init() 初始化属性，str()打印地瓜信息
#定义一个地瓜类
class DG:

    # init方法 初始化属性
    def __init__(self):
        self.cook_time = 0
        self.cook_state = "生的"
        self.condiments = []

    # 烘烤动作
    def cook(self,time):
        # 根据烘烤时间，修改地瓜状态
        if time < 0:
            print("无效值")
        # 修改地瓜的烘烤时间
        self.cook_time +=time

        if 0<= self.cook_time <3:
            print("生的")
        elif 3<= self.cook_time <7:
            print("半生不熟")
        elif 7<=self.cook_time <12:
            print("熟了")
        else:
            print("糊了")

    # 添加调料
    def add_coniments(self,coniments):
        # 添加调料到调料列表 使用的是列表.append()
        self.condiments.append(coniments)

    # 重写str方法
    def __str__(self):
        return f"烘烤时间：{self.cook_time},烘烤状态:{self.cook_state},,烘烤调料：{self.condiments}"

# 测试
if __name__ == '__main__':
    # 创建对象
    dg = DG()

    #具体的烘烤动作
    dg.cook(3)
    dg.cook(8)

    #添加调料
    dg.add_coniments("蜂蜜")

    #打印地瓜状态
    print(dg)




