# -*- coding:utf-8 -*-
from PIL import Image
import cv2
# 读入图像
img1 = cv2.imread("images/2.jpg", 0)


# # 图像降噪
# body1blur = cv2.GaussianBlur(body1, (5, 5), 0)
#
# h1blur = cv2.GaussianBlur(h1, (5, 5), 0)
# h2blur = cv2.GaussianBlur(h3, (5, 5), 0)
#
# # # Canny边缘检测，50为低阈值low，150为高阈值high
# canny1 = cv2.Canny(h1blur, 50, 150)
# canny2 = cv2.Canny(h2blur, 50, 150)

# cv2.imshow("马车", img1)


# cv2.imshow("GaussianBlur", h1blur)
# cv2.imshow("canny", canny)
# cv2.waitKey()
im = Image.fromarray(img1.astype('uint8'))
im.save("images/泥路1.jpg")
