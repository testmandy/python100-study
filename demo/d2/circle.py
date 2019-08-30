# coding=utf-8
# @Time    : 2019/8/2 17:17
# @Author  : Mandy

"""
输入圆的半径计算计算周长和面积。

"""
import math

radius = float(input('请输入圆的半径：'))

perimeter = 2*math.pi*radius
area = math.pi*radius*radius

print('圆的周长为：%.2f' % perimeter)
print('圆的面积为：%.2f' % area)


