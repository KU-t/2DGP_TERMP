import random
from pico2d import *
import game_world
import game_framework
import main_state

class Tip:
    image = None

    #def __init__(self):
    #    if Tip.image == None:
    #        Tip.image = load_image('ball21x21.png')
    #    self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0
    def __init__(self):
        self.image = load_image('TIP.png')


    def get_bb(self):
        # fill here
        return self.x - 800, self.y - 600, self.x + 800, self.y + 600

    #def draw(self):
    #    self.image.draw(self.x, self.y)
    #    # fill here for draw
    #    draw_rectangle(*self.get_bb())
    def draw(self):
        self.image.clip_draw(main_state.penguin .x - main_state.penguin.draw_x, main_state.penguin.y - main_state.penguin.draw_y, 800, 600, 400, 300)


    def update(self):
        #self.y -= self.fall_speed * game_framework.frame_time
        pass
    #fill here for def stop
    def stop(self):
        #self.fall_speed = 0
        pass
