from PIL import Image

# Open your image by specifying the path
img = Image.open("ss.png")

# Get the width and height of the image
width, height = img.size

print(f"Size (Resolution) of your Image is {width} X {height}")
