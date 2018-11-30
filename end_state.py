import game_framework
from pico2d import *
import title_state
import random
import game_world

name = "EndState"
image = None


from penguin import Penguin

penguins = []
bgm = None

def enter():
    global image
    image = load_image('./image/end.png')

    global penguins
    penguins += [Penguin(random.randint(0, 800), random.randint(0, 800)) for i in range(0, 10)]

    global bgm
    bgm = load_music('./sound/end_state.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)

def draw():
    clear_canvas()
    image.draw(400, 300)
    for penguin in penguins:
        penguin.image_wind.clip_draw(0, 0, 240, 320, penguin.x, penguin.y, 15, 20)
    update_canvas()


def update():
    for penguin in penguins:
        penguin.x = (penguin.x - (random.randint(0, 100) / 100))
        penguin.y = (penguin.y - (random.randint(0, 100) / 100))
        if penguin.x <= - 20:
            penguin.x = random.randint(0, 1200)
            penguin.y = random.randint(0, 900)
        if penguin.y <= - 20:
            penguin.x = random.randint(0, 1200)
            penguin.y = random.randint(0, 900)


def pause():
    pass


def resume():
    pass






