# 生成6名学生，5门功课的成绩，成绩范围是400~100
import pandas as pd
import numpy as np
# 设置数据集 根据numpy设置学生成绩
score_df = np.random.randint(40,100,(6,5))
# 将索引值修改为学生姓名
info = ["索旭哲","薛思雨","朱启航","王 倩","张 耀","李泽坤"]
# inf0 = ['同学' + str(i) for i in range(6)] # 六个学生
# inf0 = ['同学' + str(i) for i in range(score_df.shape(0))]  效果同上

# 将行值修改为科目
infd = ["语文","数学","英语","物理","化学"]

stu_1 = pd.DataFrame(data=score_df,index=info,columns=infd)
print(stu_1)