from pico2d import*

from location import Location
from monsters import Monsters
from menu import Menu
from coin import Coin

import game_framework
import game_shop

location = None
monsters = None
menu = None
coins = None

image_size = 1024
false = 0
true = 1

def create_world():
    global location, monsters, menu, coins
    location = Location()
    monsters = Monsters()
    menu = Menu()
    coins = [Coin() for i in range(10)]

def destroy_world():
    global location, monsters, menu, coins
    del(location)
    del(monsters)
    del(menu)
    del(coins)

def enter():
    create_world()

def exit():
    destroy_world()
    close_canvas()

def update():
    monsters.update()

def draw():
    clear_canvas()
    location.draw()
    monsters.draw()
    menu.draw()
    monsters.show_data()
    if monsters.monster_count == 2:
        for coin in coins:
            coin.draw()
            coin.draw_bb()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if (60 < event.x and event.x < 265) and (690 < event.y and event.y < 745):
                game_framework.push_state(game_shop)
            if monsters.monster_count > 1:
                for coin in coins:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        coins.remove(coin)
                        monsters.get_coin += 10
            monsters.click = true
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            monsters.click = false
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a and monsters.get_coin >= monsters.upgrade_coin:
                monsters.damage += 100
                monsters.get_coin -= monsters.upgrade_coin
                monsters.upgrade_coin = monsters.upgrade_coin * 2

def pause():
    pass

def resume():
    pass