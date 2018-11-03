import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state


name = "MainState"

font = None
tip = None
life = None

penguin = None
shoe = None
human = None

class Tip:
    def __init__(self):
        self.image = load_image('TIP.png')
    def draw(self):
        self.image.draw(400, 300)


class Life:
    def __init__(self):
        self.image = load_image('life.jpg')
        self.life = 3

    def draw(self):
        for i in range(self.life):
            self.image.clip_draw(0, 0, 512, 512, 770 - 50 * i, 570, 50, 50)


class Shoe:
    image = None

    def __init__(self):
        self.x, self.y = 400, 300
        if self.image == None:
            self.image = load_image('life.jpg')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 512, 512, self.x, self.y, 50, 50)


class Penguin:
    global shoes

    def __init__(self):
        self.x, self.y, self.move_frame, self.direct_frame = 400, 600, 0, 0
        self.draw_x, self.draw_y = 400, 300
        self.image = load_image('penguin.png')
        self.direction = [False, False, False, False]
        self.move_speed = 10
        self.life = 3
        self.state = 'move'

    def update(self):
      pass

    def draw(self):
        if self.direct_frame == 0:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x, self.draw_y - 2)
        elif self.direct_frame == 4:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 34, 45, self.draw_x + 2, self.draw_y - 4)
        elif self.direct_frame == 5:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 34, 45, self.draw_x + 5, self.draw_y - 7)
        elif self.direct_frame == 6:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x + 6, self.draw_y - 7)
        elif self.direct_frame == 7:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x + 5, self.draw_y - 4)
        else:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x, self.draw_y)


class Human:
    image = None

    def __init__(self, x, y, human_type):
        self.x = x
        self.y = y
        self.human_type = human_type
        self.state = 'sleep'
        self.frame = 0
        self.direct = 0

        if Human.image == None:
            Human.image = load_image('huddle.png')

    def draw(self):
        if self.human_type == 'red_student':
            Human.image.clip_draw(self.frame * 32 + 32 * 3, 32 * self.direct, 32, 32, self.x, self.y, 48, 48)
        elif self.human_type == 'green_student':
            Human.image.clip_draw(self.frame * 32, 32 * self.direct, 32, 32, self.x, self.y, 48, 48)
        elif self.human_type == 'blue_student':
            Human.image.clip_draw(self.frame * 32 + 32 * 3, 32 * self.direct + 32 * 4, 32, 32, self.x, self.y, 48, 48)
        elif self.human_type == 'resident':
            Human.image.clip_draw(self.frame * 32, 32 * self.direct + 32 * 4, 32, 32, self.x, self.y, 48, 48)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global boy, tip, life, penguin, shoe, human
    #boy = Boy()
    tip = Tip()
    life = Life()
    penguin = Penguin()
    shoe = Shoe()
    human = Human(200, 200, 'red_student')


def exit():
    pass
    global boy
    del(boy)


def pause():
    pass


def resume():
    pass


def handle_events():
    global penguin
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            penguin.direction[0] = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            penguin.direction[1] = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            penguin.direction[2] = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            penguin.direction[3] = True

        elif event.type == SDL_KEYUP and event.key == SDLK_UP:
            penguin.direction[0] = False
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            penguin.direction[1] = False
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            penguin.direction[2] = False
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            penguin.direction[3] = False

def update():
    #boy.update()
    pass


def draw():
    clear_canvas()
    tip.draw()
    life.draw()
    penguin.draw()
    human.draw()
    #shoe.draw()
    update_canvas()





