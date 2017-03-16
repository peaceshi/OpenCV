import cv2
import os
import numpy as np
import matplotlib.pyplot as plt  # http://matplotlib.org/api/pyplot_api.html

rootdir = r"D:\test\tepl"
templates = []
for parent, dirnames, filenames in os.walk(rootdir):
    # case 1:
    # for dirname in dirnames:
    #    print("parent folder is:" + parent)
    #    print("dirname is:" + dirname)
    #   # case 2
    for filename in filenames:
        # print("parent folder is:" + parent)
        # print("filename with full path:" + os.path.join(parent, filename))
        templates.append(os.path.join(parent, filename))

x = 0
# fpath = r'D:\test\src.png'
fpath = r'D:\test\src.png'
img = cv2.imread(fpath)  # Color image loaded by

img_rgb = cv2.imread(fpath)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
colorBGR = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 128, 0),
            (0, 128, 128), (128, 128, 128)]
for tepl in templates:
    template = cv2.imread(tepl, 0)
    # template = cv2.imread('D:/5.png', 0)

    # template = img[600:635, 755:778]
    # cv2.imwrite('template.png', template)
    # cv2.imshow("tepl", template)
    # cv2.waitKey()
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    print("current is : " + os.path.basename(tepl))
    for pt in zip(*loc[::-1]):
        # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), colorBGR[x], 2)
        print(pt)
    cv2.imwrite('res.png', img_rgb)
    # cv2.imshow("tepl", img_rgb)
    x += 1
"""
plt_img = img[..., ::-1]
plt_res = img_rgb[..., ::-1]
plt.subplot(121), plt.imshow(plt_img, cmap='gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(plt_res, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle("multiple match")

plt.show()
cv2.waitKey()
"""
