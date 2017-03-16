# -*- coding:utf-8 -*-
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html#py-display-image

import numpy as np
import os
import cv2
import matplotlib.pyplot as plt  # http://matplotlib.org/api/pyplot_api.html

# https://www.zhihu.com/question/25404709
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 有中文出现的情况，需要u'内容'


if __name__ == '__main__':
    print(cv2.__version__)

# fpath = u'D:/1111.png'
fpath = r"D:\PeaceShi\OneDrive\Pictures\HD Pic\1486472251_atelier-sophie_waifu2x_art_noise0_scale_tta_1.png"
# print(os.path.dirname(fpath).join(fpath.split()))

img = cv2.imread(fpath)  # Color image loaded by OpenCV is in BGR mode.
"""
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])
    plt.subplot(121)
    plt.imshow(img)  # expects distorted color
    plt.subplot(122)
    plt.imshow(img2)  # expect true color
    plt.show()
"""
# http://stackoverflow.com/questions/15072736/extracting-a-region-from-an-image-using-slicing-in-python-opencv/15074748#15074748
img2 = img[..., ::-1]  # same as the mentioned img[:, :, ::-1] but slightly shorter
plt.imshow(img2)
plt.title(u"凉凉")
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

