# /Library/Frameworks/Python.framework/Versions/3.10/bin/python3

'''
TODO: 백그라운드 이미지 설정
TODO: 기본값 설정
TODO: Null 들어왔을 때 예외처리
'''

from PIL import Image, ImageDraw, ImageFont, ImageColor
import datetime, json, yaml, random

class App:
    def __init__(self):
        with open('config.yml', 'r') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
            self.colors = cfg['colors']
            self.fonts = cfg['fonts']

    def input_params(self):
        self.subject = input("Enter subject name: ")
        self.title = input("Title: ")
        self.subtitle = input("Subtitle: ")
        self.author = input("Author: ")
        self.date = input("Date: ")

    def create_image(self):
        color = random.choice(self.colors)
        background_color = color['background']
        background_color = ImageColor.getrgb(color['background'])
        text_color = ImageColor.getrgb(color['text'])

        img = Image.new('RGB', (1920, 1028), color = background_color)
        draw = ImageDraw.Draw(img)

        draw.text((480, 0), self.title, fill=text_color, font=ImageFont.truetype(self.fonts['bold'], 40), align="center")
        draw.text((480, 120), self.subtitle, fill=text_color, font=ImageFont.truetype(self.fonts['light'], 40), align="center")
        draw.text((480, 240), self.author, fill=text_color, font=ImageFont.truetype(self.fonts['medium'], 40), align="center")
        draw.text((480, 360), self.date, fill=text_color, font=ImageFont.truetype(self.fonts['medium'], 40), align="center")

        img.save(f'outputs/{self.date}_{self.subject}.png')

if __name__ == "__main__":
    app = App()
    app.input_params()
    app.create_image()