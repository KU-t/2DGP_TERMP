import random
import json
import os

from pico2d import *
import game_framework
import main_state

name = "PauseState"

image = None
frame = 0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def update():
    global frame
    frame = (frame + 1) % 200


def draw():
    global image, frame
    if frame//100 == 0:
        clear_canvas()
        main_state.draw()

    if frame//100 == 1:
        image.draw(400, 300)

    update_canvas()





