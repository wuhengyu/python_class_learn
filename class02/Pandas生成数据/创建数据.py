# -*- coding: utf-8 -*-
# @Time    : 2022/6/10 14:59
# @Author  : Walter
# @File    : 创建数据.py
# @License : (C)Copyright Walter
# @Desc    :
import pandas as pd

# pd.DataFrame()为一个字典，每条数据为一个Series
# 键为表头（列索引），值为具体数据
# 生成一个DataFrame
# 系统自动加索引0、1、2
# DataFrame可以容纳Series，所以在定义DataFrame时可以使用Series
df = pd.DataFrame({'国家': ['中国', '美国', '日本'],
                   '地区': ['亚洲', '北美', '亚洲'],
                   '人口': [13.97, 3.28, 1.26],
                   'GDP': [14.34, 21.43, 5.08],
                  })

# 执行变量df的结果
# print(df)

# 返回一个Series
print(df['人口'])

# 单独创建一个Series
s = pd.Series([14.34, 21.43, 5.08], name='GDP')
print(s)