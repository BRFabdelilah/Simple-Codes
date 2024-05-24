import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread(r"images/cc/part_11.png",0)
img = cv2.resize(img, (400,400))

_,mask = cv2.threshold(img,160,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8) # 5x5 kernel with full of ones.

#All Morphological Operation.
e=cv2.erode(mask,kernel)
d=cv2.dilate(mask,kernel)
contours = cv2.findContours(d, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
o = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernel)
c = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernel, iterations=2)
x1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT, kernel)
x2 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT, kernel)
x3 = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT, kernel)

# Display images using subplots
plt.figure(figsize=[15, 10])

# Original Image
plt.subplot(331)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Mask
plt.subplot(332)
plt.imshow(mask, cmap='gray')
plt.title('Mask')
plt.axis('off')

# Erosion
plt.subplot(333)
plt.imshow(e, cmap='gray')
plt.title('Erosion')
plt.axis('off')

# Dilation
plt.subplot(334)
plt.imshow(d, cmap='gray')
plt.title('Dilation')
plt.axis('off')

# Opening
plt.subplot(335)
plt.imshow(o, cmap='gray')
plt.title('Opening')
plt.axis('off')

# Closing
plt.subplot(336)
plt.imshow(c, cmap='gray')
plt.title('Closing')
plt.axis('off')

# Tophat
plt.subplot(337)
plt.imshow(x1, cmap='gray')
plt.title('Tophat')
plt.axis('off')

# Gradient
plt.subplot(338)
plt.imshow(x2, cmap='gray')
plt.title('Gradient')
plt.axis('off')

# Blackhat
plt.subplot(339)
plt.imshow(x3, cmap='gray')
plt.title('Blackhat')
plt.axis('off')

plt.tight_layout()
plt.show()