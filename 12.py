import cv2
img = cv2.imread("Vikranth.jpg")
height ,width, channels = img.shape
print(f"The resolution of the image is {width} X {height}")
