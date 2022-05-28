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
            ymlfile.close()
        with open('content.yml', 'r') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
            content = cfg[0]
            self.subject = content['subject']
            self.title = content['title']
            self.subtitle = content['subtitle']
            self.author = content['author']
            self.date = content['date'] if content['date'] else datetime.datetime.now().strftime("%Y-%m-%d")
            ymlfile.close()

    def create_image(self):
        WIDTH = 1920
        HEIGHT = 1080
        padx, pady = 10, 10
        color = random.choice(self.colors)
        background_color = color['background']
        background_color = ImageColor.getrgb(color['background'])
        text_color = ImageColor.getrgb(color['text'])

        img = Image.new('RGB', (1920, 1028), color = background_color)
        draw = ImageDraw.Draw(img)

        noto_bold = ImageFont.truetype(self.fonts['bold'], 150)
        w1, h1 = noto_bold.getsize(text=self.title)
        draw.text(((WIDTH - w1) / 2, (HEIGHT) / 2 - h1 - pady * 2), self.title, fill=text_color, font=noto_bold)

        draw.line(xy=[((WIDTH - w1) / 2 - padx, HEIGHT / 2), ((WIDTH + w1) / 2 + padx, HEIGHT / 2)], fill=text_color, width=5)

        noto_light = ImageFont.truetype(self.fonts['light'], 80)
        w2, h2 = noto_light.getsize(text=self.subtitle)
        draw.text(((WIDTH - w2) / 2, (HEIGHT) / 2 - pady), self.subtitle, fill=text_color, font=noto_light)

        noto_light = ImageFont.truetype(self.fonts['light'], 50)
        w3, h3 = noto_light.getsize(text=f'{self.date} @{self.author}')
        draw.text(((WIDTH - w3) / 2, HEIGHT - h3 * 2 - pady), f'{self.date} @{self.author}', fill=text_color, font=noto_light)

        img.save(f'outputs/{self.date}_{self.subject}.png')

if __name__ == "__main__":
    app = App()
    app.create_image()