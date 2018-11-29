import game_framework
from pico2d import *
import main_state
import random
import end_state
import victory_state
name = "title_state"
image = None

from penguin import Penguin

penguins = []

def enter():
    global image
    image = load_image('./image/title.png')

    global penguins
    penguins = [Penguin(400, -20)]


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(400, 300)
    for penguin in penguins:
        penguin.draw_victory(3, False)
    update_canvas()


def update():
    for penguin in penguins:
        penguin.frame = (penguin.frame + 1) % 150
        if penguin.y <= 150:
            penguin.y = penguin.y + 0.1



def pause():
    pass


def resume():
    pass






