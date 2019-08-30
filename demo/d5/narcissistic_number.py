# coding=utf-8
# @Time    : 2019/8/16 10:07
# @Author  : Mandy

import math


def is_narcissistic():
    """
    判断输入的三位数是否为水仙花数
    """
    number = input('请输入三位正整数：')
    # 当输入的内容是数字，且不含小数点
    if number.isdigit() and str(number).count('.') == 0:
        n = int(number)
        # 当输入的内容长度为3
        if len(str(n)) == 3:
            a = int(n / 100)
            b = int(n / 10 - a * 10)
            c = n - a * 100 - b * 10
            if (math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3)) == n:
                print('恭喜您找到一个水仙花数！')
            else:
                print('不是水仙花数')
        else:
            print('请您输入正确的三位数')
    else:
        print('您输入的不是正整数')


def all_narcissistic():
    """
    遍历所有的水仙花数
    """
    print('所有的水仙花数：')
    for i in range(100, 1000):
        a = int(i / 100)
        b = int(i % 100 / 10)
        c = int(i % 10)
        if (math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3)) == i:
            print(i)


all_narcissistic()
