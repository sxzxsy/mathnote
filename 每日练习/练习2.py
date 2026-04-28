# 导包
import pandas as pd
import matplotlib.pyplot as plt

# 设置显示中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置正常显示符号
plt.rcParams["axes.unicode_minus"] = False

# 读取数据
df = pd.read_csv('E:/python-leran/3.数据/winemag-data_first150k.csv',index_col=0,encoding='utf-8')

# 判断是否有无缺失值，有的话用平均值替换
for col in df[['points','price']]:
    if df[col].isnull().any():
        df[col].fillna(df[col].mean(),inplace=True)  # 填充平均值 fillna : 填充  df[col]列.mean()

# 验证是否还有空值
print("填充后空值检查：")
print(df[['points', 'price']].isnull().sum())

# 创建画布
plt.figure(figsize=(20,10),dpi=80)
# 设置x,y轴
x = df['points']
y = df['price']

# 绘图
plt.scatter(x,y,color = 'r',alpha=0.5,label = '价格和评分关系图')

# 设置信息
plt.title("价格和评分关系图",fontsize=20)
plt.xlabel("评分")
plt.ylabel("价格")

# 添加网格
plt.grid(linestyle='--',color = 'black',alpha = 0.5)

# 添加图例
plt.legend(loc=0)

# 显示
plt.show()