# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 20:14
# @Author  : Walter
# @File    : 创建数据.py
# @License : (C)Copyright Walter
# @Desc    :
import numpy as np

# 列表
arr1 = np.array([1, 2, 3])
# 元组
arr2 = np.array((4, 5, 6))
# 二维元组
arr3 = np.array(((1, 2), (3, 4)))
# 元组列表
arr4 = np.array(([1, 2], [3, 4], [5, 6], [3, 4]))
# arr5 = np.array({1, 2, 3})

print(arr1)
print(arr1.shape)
print('*'*30)
print(arr2)
print(arr2.shape)
print('*'*30)
print(arr3)
print(arr3.shape)
print('*'*30)
print(arr4)
print(arr4.shape)
print('*'*30)
# 改变形状
arr4.shape = (1, 8, 1)
# 数组的形状，返回值是一个元组
print(arr4.shape)
print('*'*30)
# 改变原数组的形状，创建一个新数组
newarr = np.reshape(arr4, (1, 8, 1))
print(newarr)
print('*'*30)
# 数据类型
print(arr4.dtype)
print('*'*30)
# 维度数
print(np.ndim(arr4))
print('*'*30)
# 元素数
print(np.size(arr4))
print('*'*30)
# np的所有数据类型
print(np.typeDict['double'])
print('*'*30)
