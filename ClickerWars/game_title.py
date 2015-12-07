from pico2d import*

import game_framework
import game_main

name = "TitleState"
title = None
title_time = 0.0

def enter():
    global title
    open_canvas(480, 800)
    title = load_image('title&menu/CW_load_screen.jpg')

def exit():
    global title
    del(title)

def update():
    global title_time
    if (title_time > 1.0):
        title_time = 0
        game_framework.change_state(game_main)
    delay(0.01)
    title_time += 0.01

def draw():
    global title
    clear_canvas()
    title.draw(240, 400)
    update_canvas()

def handle_events():
    events = get_events()
    pass

def pause():
    pass

def resume():
    pass