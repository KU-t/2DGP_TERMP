import game_framework
from pico2d import *
import main_state
import random

name = "Victory"
image = None

from penguin import Penguin

penguins = []

def enter():
    global image
    image = load_image('./image/victory.png')

    global penguins
    penguins += [Penguin(random.randint(0, 800), random.randint(230, 270)) for i in range(0, 5)]

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
        penguin.draw_victory()
    update_canvas()







def update():
    pass
    global penguins

    #for penguin in penguins:



def pause():
    pass


def resume():
    pass






