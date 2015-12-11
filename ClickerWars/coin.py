from pico2d import*
import random

class COIN:
    coin = None

    def __init__(self):
        self.coin = load_image('title&menu/main6.png')

        self.x = random.randint(50, 350)

    def draw(self):
        self.coin.clip_draw(342, 759, 40, 35, self.x, 320)
