# coding=utf-8
# @Time    : 2019/8/15 11:15
# @Author  : Mandy
"""
掷骰子决定做什么事情
"""

from random import randint

face = randint(1, 6)

if face == 1:
    print('sing')
elif face == 2:
    print('dance')
elif face == 3:
    print('drink')
elif face == 4:
    print('act')
elif face == 5:
    print('jump')
elif face == 6:
    print('shopping')
else:
    print('nothing')
