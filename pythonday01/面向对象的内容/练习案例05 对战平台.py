"""
案例：演示python的多态案例，飞机战平台
需求：
1.构建对战平台（公共函数）object_play()，接收：英雄机和敌机
2.在不修改对战平台代码的情况下，完成多次战斗
3.规则：
    英雄机：1代战斗力60，二代战斗力80
    敌人机：1代战斗力70

代码提示：
    英雄机一代herfighter
    二代 avdherfighter
    敌人机enemyfighter
"""
# 定义类 一代战斗机
class herofighter:
    def power(self):
        return 60

# 定义类 2代战斗机
class avdherofighter:
    def power(self):
        return 80

# 定义类 di机
class enemyfighter:
    def power(self):
        return 70

# 构建对战平台
def duizhan(hero,enemy):

    if hero.power() <= enemy.power():
        print("惜败")
    else:
        print("赢了")

# 测试
if __name__ == '__main__':
    # 创建对象
    a1 = herofighter()
    a2 = avdherofighter()
    e = enemyfighter()

    # 第一次对战，英雄机一代对战敌人机
    duizhan(a1,e)
    #第二次
    duizhan(a2,e)