# coding=utf-8
# @Time    : 2019/8/15 10:37
# @Author  : Mandy
"""
英制单位英寸和公制单位厘米互换
"""


value = float(input('请输入长度：'))
unit = input('请输入单位：')

if unit == 'in' or unit == '英尺':
    print('%f英尺 = %f厘米'%(value, value*30.48))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英尺'%(value, value/30.48))
else:
    print('请输入有效的单位')



