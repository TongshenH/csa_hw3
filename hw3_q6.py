import cv2

# Read the image.
img = cv2.imread('left182.png')

# Apply bilateral filter
bilateral = cv2.bilateralFilter(img, 10, 80, 80)

# Save the output.
cv2.imwrite('left_bilateral.jpg', bilateral)