from PIL import Image, ImageDraw, ImageFont, ImageFilter

def main():
    try:
        # Open the image
        img = Image.open("ss.png")

        # Get image dimensions
        width, height = img.size
        print(f"Size (Resolution) of your Image is {width} X {height}")

        # Resize the image (e.g., to 200x200)
        new_width, new_height = 200, 200
        resized_image = img.resize((new_width, new_height))
        resized_image.save("resized_ss.png")

        # Apply a simple filter (e.g., blur)
        blurred_image = img.filter(ImageFilter.BLUR)
        blurred_image.save("blurred_ss.png")

        # Add text to the image
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", size=24)  # Use a font of your choice
        text = "Hello, Pillow!"
        draw.text((70, 70), text, fill="blue", font=font)
        img.save("text_overlay_ss.png")

        print("Image processing completed!")

    except FileNotFoundError:
        print("Image file not found. Make sure 'ss.png' exists in the same directory.")

if __name__ == "__main__":
    main()
