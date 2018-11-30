import random
import json
import os

from pico2d import *
import game_framework
import game_world
import end_state
import victory_state

from penguin import Penguin
from item import Item
from wall import Wall
from background import FixedBackground as Background
from map import Map
from human import Human
#from background import InfiniteBackground as Background

name = "MainState"

penguin = None
background = None
items = []
walls = []
map = None
bgm = None

def get_penguin():
    return penguin


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True


def collide_x_wall(a, wall):
    left_a, bottom_a, right_a, top_a = a.get_collision_x_bb()
    left_b, bottom_b, right_b, top_b = wall.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True


def collide_y_wall(a, wall):
    left_a, bottom_a, right_a, top_a = a.get_collision_y_bb()
    left_b, bottom_b, right_b, top_b = wall.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True

def enter():

    global background
    background = Background()
    game_world.add_object(background, 0)

    global items

    with open('./data/item_data.json', 'r') as f:
        item_data_list = json.load(f)
    for data in item_data_list:
        item = Item(data['x'], data['y'], data['type'])
        game_world.add_object(item, 1)

    global penguin
    penguin = Penguin()
    game_world.add_object(penguin, 1)

    with open('./data/human_data.json', 'r') as f:
        human_data_list = json.load(f)
    for data in human_data_list:
        human = Human(data['x'], data['y'], data['type'])
        game_world.add_object(human, 1)

    global walls
    # 세로 벽
    walls = [Wall((i + 1) * 200, 0, (i + 1) * 200, 150) for i in range(7)]
    walls += [Wall((i + 1) * 200, 300, (i + 1) * 200, 450) for i in range(5)]
    walls += [Wall((i + 1) * 200, 750, (i + 1) * 200, 900) for i in range(5)]
    walls += [Wall((i + 1) * 200, 1050, (i + 1) * 200, 1200) for i in range(7)]
    walls += [Wall(0, 0, 0, 1200), Wall(1600, 0, 1600, 1200)]

    # 가로 벽
    walls += [Wall(0, i * 150, 1600, i * 150) for i in range(9) if i == 0 or i == 8]
    walls += [Wall(0, i * 150, 1200, i * 150) for i in range(9) if i == 3 or i == 5]
    walls += [Wall(1400, i * 150, 1600, i * 150) for i in range(9) if i == 3 or i == 5]

    # 입구 벽
    walls += [Wall(-100 + 400 * i, 150, 100 + 400 * i, 150) for i in range(5)]
    walls += [Wall(-100 + 400 * i, 300, 100 + 400 * i, 300) for i in range(5) if not i == 3]
    walls += [Wall(-100 + 400 * 3, 300, 100 + 400 * 3 - 100, 300)]
    walls += [Wall(-100 + 400 * i, 900, 100 + 400 * i, 900) for i in range(5) if not i == 3]
    walls += [Wall(-100 + 400 * 3, 900, 100 + 400 * 3 - 100, 900)]
    walls += [Wall(-100 + 400 * i, 1050, 100 + 400 * i, 1050) for i in range(5)]

    # 입구 & 휴게실 & 중앙문
    walls += [Wall(1200, 300, 1200, 500), Wall(1200, 700, 1200, 900)]
    walls += [Wall(1400, 300, 1400, 500), Wall(1400, 600, 1400, 900)]
    walls += [Wall(1200, 500, 1200, 700, True)]
    game_world.add_objects(walls, 0)

    global map
    map = Map()
    game_world.add_object(map, 1)

    background.set_center_object(penguin)
    penguin.set_background(background)

    global bgm
    bgm = load_wav('./sound/main_state.wav')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    for game_object in game_world.all_objects():
        game_object.update()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            penguin.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for game_object in game_world.all_objects():
        if isinstance(game_object, Item):
            if game_object.exist:
                if collide(penguin, game_object):
                    penguin.eat(game_object)
                    #bgm.play()

    for game_object in game_world.all_objects():
        if isinstance(game_object, Human):
            if collide(penguin, game_object):
                if penguin.time_life == 0:
                    penguin.time_life = 300
                    penguin.life_count -= 1
                    penguin.hit_penguin.play(1)
                    if penguin.life_count < 0:
                        game_framework.change_state(end_state)

    if penguin.card_count >= 3:
        for game_object in game_world.all_objects():
            if isinstance(game_object, Wall):
                if game_object.door:
                    game_object.open = True

    if penguin.x <= 800:
        if 450 <= penguin.y and penguin.y <= 750:
            game_framework.change_state(victory_state)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






