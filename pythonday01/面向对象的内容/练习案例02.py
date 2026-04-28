# 需求：定义一个手机类，能开机，能关机，可以拍照
class Phone:
    # 开机方法
    def open(self):
        print(f"{self}开机")
    # 关机方法
    def off(self):
        print(f"{self}关机")
    # 拍照功能
    def picture(self):
        print(f"{self}拍照")

# 创建对象 并调用方法
phone_1 = Phone( )
print(f"1的对象：{phone_1}")
phone_1.open()
phone_1.off()
phone_1.picture()

print("*"* 50)

phone_2 = Phone( )
print(f"1的对象：{phone_2}")
phone_2.open()
phone_2.off()
phone_2.picture()