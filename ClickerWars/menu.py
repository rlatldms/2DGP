from pico2d import*

image_size = 1024
false = 0
true = 1

class Menu:
    power_state       = None
    coin_state        = None
    coin              = None
    shop              = None

    here_map          = None
    next_map          = None
    here_arrow        = None

    def __init__(self):
        self.power_state = load_image('title&menu/main6.png')
        self.coin_state = load_image('title&menu/main6.png')
        self.coin = load_image('title&menu/main6.png')
        self.shop = load_image('title&menu/main6.png')

        self.here_map = load_image('title&menu/main6.png')
        self.next_map = load_image('title&menu/main6.png')
        self.here_arrow = load_image('title&menu/main6.png')

    def draw(self):
        self.power_state.clip_draw(455, 0, 485, 190, 240, 80)
        self.coin_state.clip_draw(0, image_size - 550, 340, 60, 240, 775)
        self.coin.clip_draw(342, image_size - 265, 40, 35, 140, 770)
        self.coin.clip_draw(342, image_size - 265, 40, 35, 120, 770)
        self.shop.clip_draw(760, image_size - 835, 210, 60, 160, 80)

        self.here_map.clip_draw(565, image_size - 514, 90, 75, 240, 700)
        self.next_map.clip_draw(940, image_size - 910, 90, 75, 330, 700)
        self.here_arrow.clip_draw(755, image_size - 620, 35, 60, 240, 680)
