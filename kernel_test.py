import cv2
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

bgr_img = cv2.imread('lenna.png')
# OpenCV uses BGR. Convert back to RGB.
rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)

# Pick kernel to use.
identitiy_kernel = np.array([[0,0,0],
                             [0,1,0],
                             [0,0,0]])
question_kernel = np.array([[1,1,1],
                            [1,-8,1],
                            [1,1,1]])
sharpen_kernel = np.array([[0,-1,0],
                           [-1,5,-1],
                           [0,-1,0]])


question_kernel_img = cv2.filter2D(gray_img,-1, question_kernel)
sharpen_kernel_img = cv2.filter2D(gray_img,-1, sharpen_kernel)

fig=plt.figure(figsize=(2, 2))


fig.add_subplot(2, 2, 1), plt.imshow(rgb_img), plt.title('Original'), plt.xticks([]), plt.yticks([]) #remove ticks
fig.add_subplot(2, 2, 2), plt.imshow(gray_img, cmap="gray"),plt.title('Gray'), plt.xticks([]), plt.yticks([]) #remove ticks
fig.add_subplot(2, 2, 3), plt.imshow(question_kernel_img, cmap="gray"), plt.title('Filtered'), plt.xticks([]), plt.yticks([]) #remove ticks
fig.add_subplot(2, 2, 4), plt.imshow(sharpen_kernel_img, cmap="gray"), plt.title('Sharpened'), plt.xticks([]), plt.yticks([]) #remove ticks

plt.show()
