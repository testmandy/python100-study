# coding=utf-8
# @Time    : 2019/8/15 11:56
# @Author  : Mandy
"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
"""
import math

a = float(input('请输入三角形的边长：a = '))
b = float(input('请输入三角形的边长：b = '))
c = float(input('请输入三角形的边长：c = '))

if a+b > c and b+c > a and a+c > b:
    print("此三边可以构成三角形")
    perimeter = a+b+c
    p = perimeter/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))

    print('三角形的周长为：%0.2f' % perimeter)
    print('三角形的面积为：%0.2f' % area)
else:
    print('您输入的三个边长无法构成三角形')


