from pico2d import*
from game_object import OBJECT
from coin import COIN
import game_framework

object = None

image_size = 1024
F = 0
T = 1

def create_world():
    global object, coins
    object = OBJECT()
    coins = [COIN() for i in range(10)]

def destroy_world():
    global object, coins
    del(object)
    del(coins)

def enter():
    create_world()

def exit():
    destroy_world()
    close_canvas()

def update():
    object.update()

def draw():
    clear_canvas()
    object.draw()
    object.data()
    if object.monsters_count > 1:
        for coin in coins:
            coin.draw()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            object.click = T

            if object.monsters_count > 1:
                for coin in coins:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        object.eat_coin += 10
                        coins.remove(coin)

        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            object.click = F

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a and object.eat_coin >= object.skill_upgrade:
                object.my_damage += 10
                object.eat_coin -= object.skill_upgrade
                object.skill_upgrade = object.skill_upgrade * 2

def pause():
    pass

def resume():
    pass