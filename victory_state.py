import game_framework
from pico2d import *
import game_world

import main_state
import random

name = "Victory"
image = None

from penguin import Penguin

penguins = []
bgm = None

def enter():
    global image
    image = load_image('./image/victory.png')

    global penguins
    penguins += [Penguin(i * 180, random.randint(230, 270)) for i in range(0, 5)]

    global bgm
    bgm = load_music('./sound/victory_state.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    game_world.clear()
    bgm.stop()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.quit()

def draw():
    clear_canvas()
    image.draw(400, 300)
    for penguin in penguins:
        penguin.frame = (penguin.frame + 1) % 150
        penguin.x = (penguin.x - (random.randint(0, 100) / 100))
        if penguin.x <= - 20:
            penguin.x = 820
            penguin.y = random.randint(230, 270)
        penguin.draw_victory(5, True)
    update_canvas()


def update():
    pass


    #for penguin in penguins:


def pause():
    pass


def resume():
    pass






