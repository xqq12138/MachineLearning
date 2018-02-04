# -*- coding: utf-8 -*-
from handwriting.imgToTxt import ImgToTxt
from kNN import KNN

# KNN().handwritingClassTest(234)
# 图片 自己写的数字
ImgToTxt().conv('tmp.png')
KNN().testHandwritingClassTest('test.txt')
