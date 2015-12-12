from pico2d import*
from game_object import OBJECT
import game_framework

image_size = 1024

def create_world():
    global object
    object = OBJECT()

def destroy_world():
    global object
    del(object)
def enter():
    create_world()

def exit():
    destroy_world()
    close_canvas()

def update():
    object.update()

def draw():
    clear_canvas()
    object.location()
    object.monsters()
    if object.drop_coin[object.stage - 1][object.monsters_count - 1] == True:
        object.coins()
    object.draw()
    object.draw_data()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            object.click = True
            #object.sound_click.play()
            if object.drop_coin[object.stage - 1][object.monsters_count - 1] == True:
                if (object.coinX - 18 < event.x and event.x < object.coinX + 15) and (465 < event.y and event.y < 495):
                    #object.sound_eatCoin.play()
                    object.eat_coin += 100
                    object.drop_coin[object.stage - 1][object.monsters_count - 1] = False

        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            object.click = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a and object.eat_coin >= object.skill_upgrade:
                #object.sound_upgrage.play()
                object.my_damage += 5
                object.eat_coin -= object.skill_upgrade
                object.skill_upgrade += 100 * object.stage
            if event.key == SDLK_q:
                object.my_damage += 100

def pause():
    pass

def resume():
    pass