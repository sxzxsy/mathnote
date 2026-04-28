# 类和对象的关系：

# 定义一个闹钟类
class clock():
    id = None
    price = None
    # 构建闹钟的行为
    def reading(self):
        # 调用一个响铃的包
        import  winsound
        winsound.Beep(2000,3000)

    # 类内部调用
    def r(self):
        print(f"{self.id}",f"{self.price}")

# 基于类创建对象
clock_1 = clock()
clock_1.id = 1234
clock_1.price = 19.99

# 数据内容输出
print(f"这个闹钟的编号是{clock_1.id},价格是{clock_1.price}")
# 调用方法，让其工作
clock_1.reading()