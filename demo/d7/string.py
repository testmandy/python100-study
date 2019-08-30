# coding=utf-8
# @Time    : 2019/8/21 11:18
# @Author  : Mandy
"""
所谓字符串，就是由零个或多个字符组成的有限序列，一般记为displaystyle sa1a2dots an0leq n leq infty。
"""


def main():
    str1 = 'hello, world!'
    # 通过len函数计算字符串的长度
    print('str1的长度为：%d' % len(str1))
    # 获得字符串首字母大写的拷贝
    print('str1的首字母大写为：%s' % str1.capitalize())
    # 获得字符串变大写后的拷贝
    print('str1的大写格式为：%s' % str1.upper())
    # 从字符串中查找子串所在位置
    print('str1中or的位置为：%d' % str1.find('or'))
    print('str1中shit的位置为：%d' % str1.find('shit'))
    # 使用index方法从字符串中查找子串所在位置-找不到会报错
    # print('str1中or的位置为：%d' % str1.index('or'))
    # print('str1中shit的位置为：%d' % str1.index('shit'))
    # 检查字符串是否以指定的字符串开头
    print('str1是否以he开头：%s' % str1.startswith('he'))
    print('str1是否以wo开头：%s' % str1.startswith('wo'))
    # 检查字符串是否以指定的字符串结尾
    print('str1是否以!结尾：%s' % str1.endswith('!'))
    print('str1是否以wo结尾：%s' % str1.endswith('wo'))
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print('str1居中并填充：%s' % str1.center(30, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print('str1右对齐并填充：%s' % str1.rjust(30, '*'))

    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print('str2取字符：%s' % str2[2])
    # 字符串切片
    print('str2取字符串：%s' % str2[2:5])
    print('str2取字符串：%s' % str2[::])
    print('str2取字符串：%s' % str2[::-1])
    # 检查字符串是否由数字构成
    print('str2是否由数字构成：%s' % str2.isdigit())
    # 检查字符串是否以字母构成
    print('str2是否由字母构成：%s' % str2.isalpha())
    # 检查字符串是否以数字和字母构成
    print('str2是否由字母和数字构成：%s' % str2.isalnum())

    str3 = '         ABC D  '
    # 获得字符串修剪左右两侧空格的拷贝
    print('str3去除前后空格：%s' % str3.strip())
    # 替换字符串中的字符
    print('str3替换空格：%s' % str3.replace(' ', '*'))
    print('str3去除前后空格后再替换空格：%s' % str3.strip().replace(' ', '*'))


if __name__ == '__main__':
    main()
