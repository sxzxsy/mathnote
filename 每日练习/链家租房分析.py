import pandas as pd
import matplotlib.pyplot as plt



# 设置显示中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置正常显示符号
plt.rcParams["axes.unicode_minus"] = False

# 读取数据
# 导入数据csv格式的数据集
df =pd.read_csv('E:/python-leran/3.数据/LJdata.csv',index_col=0,encoding='utf-8')
# 查看数据集信息
# df.info() # 查看数据集信息
# df.describe()  # 查看数据集描述信息
# # 需求做出面积和价格关系图
# 先判断面积和价格中有没有空值，
for i in df[['面积','价格']]:
    # 判断面积和价格有无空值
    if df[i].isnull().any():
        df[i].fillna(df[i].mean(),inplace=True)

# 创建画布
fig,axes = plt.subplots(1,2,figsize=(20,10),dpi=80)
# 添加数据 x,y
x = df['面积'][50:150] # 前100条数据
y_price= df['价格'][50:150]
y_num = df['看房人数'][50:150]
# 绘制柱状图
axes[0].scatter(x,y_price,color = 'r',alpha=0.5)
axes[1].bar(x,y_num,color = 'g',alpha=0.5)

# 添加网格
axes[0].grid(linestyle = '--',color = 'black',alpha = 0.5)
axes[1].grid(linestyle = '--',color = 'black',alpha = 0.5)

# 添加标题 左右都要
# 左边
axes[0].set_title("面积和价格关系图",fontsize=20)
axes[0].set_xlabel("面积")
axes[0].set_ylabel("价格")
# 右边
axes[1].set_title("面积和看房人数关系图",fontsize=20)
axes[1].set_xlabel("面积")
axes[1].set_ylabel("看房人数")

# 图例
axes[0].legend(loc = 0)
axes[1].legend(loc = 0)
# 显示
plt.show()




