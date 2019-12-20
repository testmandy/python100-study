# coding=utf-8
# @Time    : 2019/12/3 14:19
# @Author  : Mandy

from PIL import Image


image = Image.open('../resources/deer.jpg')
image.format, image.size, image.mode
image.show()

