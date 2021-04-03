# Samarth Srivastava
# 18BCE10232
# Animate your photo using opencv library in python

import cv2
image = cv2.imread("original.jpg")  # this will load the image into image variable from root directory
grey_img = cv2.cvtColor(image, cv2.COLOR_BGRA2YUV_YV12)  # add grey filter
invert = cv2.bitwise_not(grey_img)  # invert colours of our image
blur = cv2.GaussianBlur(invert, (21,21), 0)  # blur effect
inverted_blur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, inverted_blur, scale = 256.0)

# save our image file
cv2.imwrite("animated.png", sketch)
# new file named as "animated.png"
