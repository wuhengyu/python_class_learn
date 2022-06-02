# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 00:46
# @Author  : Walter
# @File    : demo.py
# @License : (C)Copyright Walter
# @Desc    :
import pandas as pd  # 引入Pandas库，按惯例起别名pd

# 以下两种效果一样，如果是网址，它会自动将数据下载到内存
# df = pd.read_excel('https://www.gairuo.com/file/data/dataset/team.xlsx')

df = pd.read_excel('team.xlsx', 'Sheet1')  # 文件在notebook文件同一目录下
# 如果是CSV，使用pd.read_csv()，还支持很多类型的数据读取
df.head() # 查看前5条，括号里可以写明你想看的条数
df.tail() # 查看尾部5条
df.sample(5) # 随机查看5条
print(df.sample(5))

# df.shape()
# df.info() # 查看索引、数据类型和内存信息
# df.describe() # 查看数值型列的汇总统计
# df.dtypes  # 查看各字段类型
# df.axes()  # 显示数据行和列名
# var = df.columns  # 列名
df.info()