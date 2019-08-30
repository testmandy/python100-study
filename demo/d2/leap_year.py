# coding=utf-8
# @Time    : 2019/8/14 16:01
# @Author  : Mandy
"""
输入年份 如果是闰年输出True 否则输出False

"""


year = int(input('请输入年份：'))
flag = None
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    flag = True
    print("您输入的年份是：闰年")
else:
    flag = False
    print("您输入的年份是：平年")
# print(flag)
