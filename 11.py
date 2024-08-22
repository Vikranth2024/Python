from PIL import Image, ImageDraw, ImageFont, ImageFilter

def main():
    try:
        img = Image.open("ss.png")
        width, height = img.size

        new_width, new_height = 200, 200
        resized_image = img.resize((new_width, new_height))
        resized_image.save("resized_ss.png")

        blurred_image = img.filter(ImageFilter.BLUR)
        blurred_image.save("blurred_ss.png")

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", size=24)
        text = "Hello, Pillow!"
        draw.text((70, 70), text, fill="blue", font=font)
        img.save("text_overlay_ss.png")

    except FileNotFoundError:
        print("Image file not found. Make sure 'ss.png' exists in the same directory.")

