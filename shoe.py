import random
from pico2d import *
import game_world
import game_framework
import main_state


class Shoe:
    image = None

    #def __init__(self):
    #    if Tip.image == None:
    #        Tip.image = load_image('ball21x21.png')
    #    self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0
    def __init__(self, x = 400, y = 300):
        self.x, self.y = x, y
        if Shoe.image == None:
            Shoe.image = load_image('life.jpg')


    def get_bb(self):
        # fill here
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    #def draw(self):
    #    self.image.draw(self.x, self.y)
    #    # fill here for draw
    #    draw_rectangle(*self.get_bb())
    def draw(self):
        self.image.clip_draw(0, 0, 512, 512, self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())

    def update(self):
        #self.y -= self.fall_speed * game_framework.frame_time
        pass
    #fill here for def stop
    def stop(self):
        #self.fall_speed = 0
        pass
