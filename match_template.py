import numpy as np
import cv2
# print(dir(cv2))
import matplotlib.pyplot as plt  # http://matplotlib.org/api/pyplot_api.html

fpath = u'D:/1111.png'
# fpath = r"D:\PeaceShi\OneDrive\Pictures\HD Pic\1486472251_atelier-sophie_waifu2x_art_noise0_scale_tta_1.png"
# print(os.path.dirname(fpath).join(fpath.split()))

img = cv2.imread(fpath)  # Color image loaded by Opencv2 is in BGR mode.
img2 = img.copy()
"""# create one window
win_name = "test"
cv2.namedWindow(win_name)
win2_name = "test2"
cv2.namedWindow(win2_name)
"""
# take off one template
# rect = (170, 80, 50, 50)
# cv2.setimageroi(image, rect)
# image[c1:c1+25,r1:r1+25]
# template = cv2.cloneImage(image)
# cv2.showImage(win_name, template)

# template = img[896:1460, 732:1321]
template = img[600:635, 755:778]
w, h = template.shape[1] - 1, template.shape[0] -1
cv2.imshow("tepl", template)
cv2.waitKey()
#exit(0)
"""
cv2.imshow(win_name, template)
print(dir(image.size))
cv2.waitKey()
#cv2.resetImageROI(image)
#W, H = cv2.getSize(image)
#w, h = cv2.getSize(template)
#width = W - w + 1
#height = H - h + 1
# result = cv2.createImage((width, height), 32, 1)

width, height = image.shape[1] -template.shape[1] +1, image.shape[0] - template.shape[0] + 1
# http://stackoverflow.com/questions/12881926/create-a-new-rgb-opencv-image-using-python
result = np.zeros((width, height, 3), np.uint8)
# result是一个矩阵，存储了模板与源图像每一帧相比较后的相似值，
cv2.matchTemplate(image, template, result, cv2.TM_SQDIFF)

# 下面的操作将从矩阵中找到相似值最小的点，从而定位出模板位置
(min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
(x, y) = minloc
cv2.rectangle(image, (int(x), int(y)), (int(x) + w, int(y) + h), (255, 255, 255), 1, 0)
cv2.showImage(win2_name, image)

cv2.waitKey()
"""
# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    plt_img = img[..., ::-1]
    plt_res = res[..., ::-1]
    plt.subplot(121), plt.imshow(plt_res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(plt_img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
