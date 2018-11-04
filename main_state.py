import random
import json
import os

from pico2d import *
import game_framework
import game_world

from penguin import Penguin
#from grass import Grass
from tip import Tip
from life import Life

name = "MainState"

penguin = None
tip = None
life = None
#balls = []
#big_balls = []


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True




def enter():
    global penguin
    penguin = Penguin()
    game_world.add_object(penguin, 1)

    global tip
    tip = Tip()
    game_world.add_object(tip, 0)

    global life
    life = Life()
    game_world.add_object(life, 0)

    # fill here for balls
    #global balls
    #balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]
    #game_world.add_objects(balls, 1)




def exit():
    game_world.clear()

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
        #else:
            #boy.handle_event(event)
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
    for game_object in game_world.all_objects():
        game_object.update()
    update_obj()

    # fill here for collision check
    #for ball in balls:
    #    if collide(boy, ball):
    #        balls.remove(ball)
    #        game_world.remove_object(ball)
    #for ball in balls:
    #    if collide(grass, ball):
    #        ball.stop()

    #delay(0.2)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()



def move_obj():
    if penguin.direction[0] == True:
        if penguin.direction[1] == True:
            count_x_decrease()
            count_y_increase()
            penguin.direct_frame = 4
        elif penguin.direction[2] == True:
            pass
        elif penguin.direction[3] == True:
            count_x_increase()
            count_y_increase()
            penguin.direct_frame = 2
        else:
            count_y_increase()
            penguin.direct_frame = 3



    elif penguin.direction[1] == True:
        if penguin.direction[2] == True:
            count_x_decrease()
            count_y_decrease()
            penguin.direct_frame = 6
        elif penguin.direction[3] == True:
            pass
        else:
            count_x_decrease()
            penguin.direct_frame = 5

    elif penguin.direction[2] == True:
        if penguin.direction[3] == True:
            count_x_increase()
            count_y_decrease()
            penguin.direct_frame = 0
        else:
            count_y_decrease()
            penguin.direct_frame = 7

    elif penguin.direction[3] == True:
        count_x_increase()
        penguin.direct_frame = 1





def update_obj():
    #penguin.move_frame = (penguin.move_frame + 1) % 8
    #penguin.move_frame = (int)(penguin.move_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
    #for student in students:
    #    student.frame = (student.frame + 1) % 3
    #    if student.frame == 0:
    #        student.direct = random.randrange(0, 4)
    #for resident in residents:
    #    resident.frame = (resident.frame + 1) % 3
    #    #resident.x += 5;
    #    if resident.frame == 0:
    #        resident.direct = random.randrange(0, 4)

    move_obj()







def count_x_increase():

    if penguin.x >= 1200:
        if penguin.x < 1590:
            penguin.draw_x += penguin.move_speed
            #shoe.x += penguin.move_speed
            #for student in students:
            #    student.x += penguin.move_speed
            #for resident in residents:
            #    resident.x += penguin.move_speed



    elif penguin.x < 400:
        if penguin.x >= 10:
            penguin.draw_x += penguin.move_speed
            #shoe.x += penguin.move_speed
            #for student in students:
            #    student.x += penguin.move_speed
            #for resident in residents:
            #    resident.x += penguin.move_speed



    if penguin.x < 1590:
        penguin.x += penguin.move_speed
        #shoe.x -= penguin.move_speed
        #for student in students:
        #    student.x -= penguin.move_speed
        #for resident in residents:
        #    resident.x -= penguin.move_speed



def count_y_increase():

    if penguin.y >= 900:
        if penguin.y < 1180:
            penguin.draw_y += penguin.move_speed
            #shoe.y += penguin.move_speed
            #for student in students:
            #    student.y += penguin.move_speed
            #for resident in residents:
            #    resident.y += penguin.move_speed



    elif penguin.y >= 20:

        if penguin.y < 300:
            penguin.draw_y += penguin.move_speed
            #shoe.y += penguin.move_speed
            #for student in students:
            #    student.y += penguin.move_speed
            #for resident in residents:
            #    resident.y += penguin.move_speed



    if penguin.y < 1180:
        penguin.y += penguin.move_speed
        #shoe.y -= penguin.move_speed
        #for student in students:
        #    student.y -= penguin.move_speed
        #for resident in residents:
        #   resident.y -= penguin.move_speed





def count_x_decrease():

    if penguin.x <= 400:
        if penguin.x > 10:
            penguin.draw_x -= penguin.move_speed
            #shoe.x -= penguin.move_speed
            #for student in students:
            #    student.x -= penguin.move_speed
            #for resident in residents:
            #    resident.x -= penguin.move_speed



    elif penguin.x > 1200:

        if penguin.x <= 1590:
            penguin.draw_x -= penguin.move_speed
            #shoe.x -= penguin.move_speed
            #for student in students:
            #    student.x -= penguin.move_speed
            #for resident in residents:
            #    resident.x -= penguin.move_speed



    if penguin.x > 10:
        penguin.x -= penguin.move_speed
        #shoe.x += penguin.move_speed
        #for student in students:
        #    student.x += penguin.move_speed
        #for resident in residents:
        #       resident.x += penguin.move_speed



def count_y_decrease():
    if penguin.y > 900:
        if penguin.y <= 1180:
            penguin.draw_y -= penguin.move_speed
        #    shoe.y -= penguin.move_speed
        #    for student in students:
        #        student.y -= penguin.move_speed
        #    for resident in residents:
        #        resident.y -= penguin.move_speed



    elif penguin.y > 20:
        if penguin.y <= 300:
            penguin.draw_y -= penguin.move_speed
        #    shoe.y -= penguin.move_speed
        #    for student in students:
        #        student.y -= penguin.move_speed
        #    for resident in residents:
        #        resident.y -= penguin.move_speed



    if penguin.y > 20:
        penguin.y -= penguin.move_speed
        #shoe.y += penguin.move_speed
        #for student in students:
        #    student.y += penguin.move_speed
        #for resident in residents:
        #    resident.y += penguin.move_speed





