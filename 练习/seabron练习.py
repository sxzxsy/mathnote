# 导包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 导入数据
df =pd.read_csv("E:/data/breast-cancer-wisconsin.csv")
print(df.info())
print(df.describe())

# 数据可视化
fig , axes = plt.subplots(figsize=(20,10),dpi=80)

sns.countplot(data=df ,x='Mitoses',hue='Class')
# 设置x轴标签
plt.xlabel('Mitoses')
plt.title('Mitoses')
plt.show()