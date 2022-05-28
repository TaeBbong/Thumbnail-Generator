# /Library/Frameworks/Python.framework/Versions/3.10/bin/python3

from PIL import Image, ImageDraw, ImageFont
import datetime, json, yaml, random

class App:
    def __init__(self):
        with open('config.yml', 'r') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
            self.colors = cfg['colors']

    def input_params(self):
        self.subject = input("Enter subject name: ")
        self.title = input("Title: ")
        self.subtitle = input("Subtitle: ")
        self.author = input("Author: ")
        self.date = input("Date: ")

    def create_image(self):
        img = Image.new('RGB', (1920, 1028), color = 'white')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 40)
        draw.text((480, 240), "Hello World", fill=(255, 0, 0), font=font, align="center")
        img.save(f'{self.date}_{self.subject}.png')

if __name__ == "__main__":
    app = App()
    # app.input_params()
    # app.create_image()