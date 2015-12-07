from pico2d import*

import random

image_size = 1024

class Coin:
    coin = None

    def __init__(self):
        self.coin = load_image('title&menu/main6.png')

        self.x = random.randint(50, 350)

    def draw(self):
        self.coin.clip_draw(342, image_size - 265, 40, 35, self.x, 320)

    def get_bb(self):
        return self.x - 18, 800 - 465, self.x + 15, 800 - 495

    def draw_bb(self):
        draw_rectangle(*self.get_bb())