from pico2d import*

import game_framework

title = None
shop = None

image_size = 1024
image_size2 = 256

class Shop:
    coin_state    = None
    coin          = None

    shop_state = None
    click_damage = None
    unfilled_skill_state = None
    filled_skill_state = None

    shop_exit     = None

    upgrade_click_damage = 0

    def __init__(self):
        self.coin_state = load_image('title&menu/main6.png')
        self.coin = load_image('title&menu/main6.png')

        self.shop_state = load_image('title&menu/shop.png')
        self.skill_click_damage = load_image('title&menu/shop.png')
        self.unfilled_skill_state = load_image('title&menu/shop.png')
        self.filled_skill_state = load_image('title&menu/shop.png')

        self.shop_exit = load_image('title&menu/shop4.png')

    def draw(self):
        self.coin_state.clip_draw(0, image_size - 550, 340, 60, 240, 775)
        self.coin.clip_draw(342, image_size - 260, 40, 35, 140, 775)
        self.coin.clip_draw(342, image_size - 260, 40, 35, 120, 775)

        self.shop_state.clip_draw(0, image_size2 - 250, 465, 95, 240, 640)
        self.shop_state.clip_draw(0, image_size2 - 250, 465, 95, 240, 550)
        self.shop_state.clip_draw(0, image_size2 - 250, 465, 95, 240, 460)
        self.shop_state.clip_draw(0, image_size2 - 250, 465, 95, 240, 370)
        self.shop_state.clip_draw(0, image_size2 - 250, 465, 95, 240, 280)
        self.shop_state.clip_draw(0, image_size2 - 250, 465, 95, 240, 190)
        self.shop_state.clip_draw(0, image_size2 - 250, 465, 95, 240, 100)
        self.skill_click_damage.clip_draw(395, image_size2 - 155, 75, 75, 55, 640)
        self.unfilled_skill_state.clip_draw(550, image_size2 - 170, 15, 35, 110, 620)
        self.unfilled_skill_state.clip_draw(550, image_size2 - 170, 15, 35, 130, 620)
        self.unfilled_skill_state.clip_draw(550, image_size2 - 170, 15, 35, 150, 620)
        self.unfilled_skill_state.clip_draw(550, image_size2 - 170, 15, 35, 170, 620)
        self.unfilled_skill_state.clip_draw(550, image_size2 - 170, 15, 35, 190, 620)
        if self.upgrade_click_damage == 1:
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 110, 620)
        if self.upgrade_click_damage == 2:
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 110, 620)
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 130, 620)
        if self.upgrade_click_damage == 3:
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 110, 620)
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 130, 620)
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 150, 620)
        if self.upgrade_click_damage == 4:
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 130, 620)
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 110, 620)
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 150, 620)
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 170, 620)
        if self.upgrade_click_damage == 5:
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 110, 620)
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 130, 620)
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 150, 620)
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 170, 620)
            self.filled_skill_state.clip_draw(503, image_size2 - 47, 15, 35, 190, 620)
        self.shop_exit.clip_draw(605, image_size - 370, 37, 35, 450, 775)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 17, 605, 90, 677

def enter():
    global title, shop
    title = load_image('title&menu/CW_load_screen.jpg')
    shop = Shop()

def exit():
    global title, shop
    del(title)
    del(shop)

def update():
    pass

def draw():
    global title, shop
    clear_canvas()
    title.draw(240, 400)
    shop.draw()
    shop.draw_bb()
    update_canvas()

def handle_events():
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            if (432 < event.x and event.x < 468) and (9 < event.y and event.y < 43):
                game_framework.pop_state()
            if (17 < event.x and event.x < 90) and (123 < event.y and event.y < 195):
                if shop.upgrade_click_damage < 5:
                    shop.upgrade_click_damage += 1
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            pass

def pause():
    pass

def resume():
    pass