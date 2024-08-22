import cv2
img = cv2.imread("Vikranth.jpg")    
height, width, channels = img.shape
print(f"Size (Resolution) of your Image is {width} X {height}")
print(channels)
