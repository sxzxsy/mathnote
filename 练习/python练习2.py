# 要求编写一下啊多态场景，飞机大战

# fly1 = 英雄战机
# fly2 = 敌方战机
# fly3 =英雄战机二代
class fly:
    def power(self):
        return 60
class dfly :
    def power(self):
        return 70
class fly02 :
    def power(self):
        return 80


# 构建飞机对战平台
def object(hero , enemy):
    if hero.power() >= enemy.power():
        print("英雄战机胜利")
    else:
        print("敌方战机胜利")
# 创建对象
f1 = fly()
f2 = dfly()
f3 = fly02()

# 调用方法
object(f1,f2)
object(f3,f2)

