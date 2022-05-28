# /Library/Frameworks/Python.framework/Versions/3.10/bin/python3

from PIL import Image, ImageDraw, ImageFont

class App:
    def __init__(self):
        pass

    def create_image(self, filename):
        img = Image.new('RGB', (200, 200), color = 'white')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 40)
        draw.text((100, 100), "Hello World", fill=(255, 0, 0), font=font)
        img.save(filename)

if __name__ == "__main__":
    app = App()
    app.create_image('test.png')