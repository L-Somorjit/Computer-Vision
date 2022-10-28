import cv2
import matplotlib.pyplot as plt

im = cv2.imread('road.jpg')
l, h = (im.shape[:2]) #length and height of image

im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# print(im.shape)
# im_resize = cv2.resize(im,(800,800))

x = plt.imshow(im_rgb)

plt.show()

# print(im_resize.shape)

# cv2.imshow("resize",im_resize)
# cv2.waitKey()
# cv2.destroyAllWindows()