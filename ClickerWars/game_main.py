from pico2d import*
from game_object import OBJECT
from coin import COIN
import game_framework

object = None

image_size = 1024
F = 0
T = 1

def create_world():
    global object, coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10
    object = OBJECT()
    if object.stage == 1:
        coin1 = [COIN() for i in range(10)]
        coin2 = [COIN() for i in range(10)]
        coin3 = [COIN() for i in range(10)]
        coin4 = [COIN() for i in range(10)]
        coin5 = [COIN() for i in range(10)]
        coin6 = [COIN() for i in range(10)]
        coin7 = [COIN() for i in range(10)]
        coin8 = [COIN() for i in range(10)]
        coin9 = [COIN() for i in range(10)]
        coin10 = [COIN() for i in range(10)]
    if object.stage == 2:
        coin1 = [COIN() for i in range(10)]
        coin2 = [COIN() for i in range(10)]
        coin3 = [COIN() for i in range(10)]
        coin4 = [COIN() for i in range(10)]
        coin5 = [COIN() for i in range(10)]
        coin6 = [COIN() for i in range(10)]
        coin7 = [COIN() for i in range(10)]
        coin8 = [COIN() for i in range(10)]
        coin9 = [COIN() for i in range(10)]
        coin10 = [COIN() for i in range(10)]
    if object.stage == 3:
        coin1 = [COIN() for i in range(10)]
        coin2 = [COIN() for i in range(10)]
        coin3 = [COIN() for i in range(10)]
        coin4 = [COIN() for i in range(10)]
        coin5 = [COIN() for i in range(10)]
        coin6 = [COIN() for i in range(10)]
        coin7 = [COIN() for i in range(10)]
        coin8 = [COIN() for i in range(10)]
        coin9 = [COIN() for i in range(10)]
        coin10 = [COIN() for i in range(10)]

def destroy_world():
    global object, coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10
    del(object)
    del(coin1)
    del(coin2)
    del(coin3)
    del(coin4)
    del(coin5)
    del(coin6)
    del(coin7)
    del(coin8)
    del(coin9)
    del(coin10)

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
    if object.monsters_count == 2:
        for coin in coin1:
            coin.draw()
    if object.monsters_count == 3:
        for coin in coin2:
            coin.draw()
    if object.monsters_count == 4:
        for coin in coin3:
            coin.draw()
    if object.monsters_count == 5:
        for coin in coin4:
            coin.draw()
    if object.monsters_count == 6:
        for coin in coin5:
            coin.draw()
    if object.monsters_count == 7:
        for coin in coin6:
            coin.draw()
    if object.monsters_count == 8:
        for coin in coin7:
            coin.draw()
    if object.monsters_count == 9:
        for coin in coin8:
            coin.draw()
    if object.monsters_count == 10:
        for coin in coin9:
            coin.draw()
    if object.monsters_count == 11:
        for coin in coin10:
            coin.draw()

    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            object.click = T

            if object.monsters_count == 2:
                for coin in coin1:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        object.eat_coin += 10
                        coin1.remove(coin)
            if object.monsters_count == 3:
                for coin in coin2:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        object.eat_coin += 10
                        coin2.remove(coin)
            if object.monsters_count == 4:
                for coin in coin3:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        object.eat_coin += 10
                        coin3.remove(coin)
            if object.monsters_count == 5:
                for coin in coin4:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        object.eat_coin += 10
                        coin4.remove(coin)
            if object.monsters_count == 6:
                for coin in coin5:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        object.eat_coin += 10
                        coin5.remove(coin)
            if object.monsters_count == 7:
                for coin in coin6:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        object.eat_coin += 10
                        coin6.remove(coin)
            if object.monsters_count == 8:
                for coin in coin7:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        object.eat_coin += 10
                        coin7.remove(coin)
            if object.monsters_count == 9:
                for coin in coin8:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        object.eat_coin += 10
                        coin8.remove(coin)
            if object.monsters_count == 10:
                for coin in coin9:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        object.eat_coin += 10
                        coin9.remove(coin)
            if object.monsters_count == 11:
                for coin in coin10:
                    if (coin.x - 18 < event.x and event.x < coin.x + 15) and (465 < event.y and event.y < 495):
                        object.eat_coin += 10
                        coin10.remove(coin)

        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            object.click = F

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a and object.eat_coin >= object.skill_upgrade:
                object.my_damage += 5
                object.eat_coin -= object.skill_upgrade
                object.skill_upgrade = object.skill_upgrade * 2

def pause():
    pass

def resume():
    pass