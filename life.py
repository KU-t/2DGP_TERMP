import random
from pico2d import *
import game_world
import game_framework
import main_state

class Life:

    #def __init__(self):
    #    if Tip.image == None:
    #        Tip.image = load_image('ball21x21.png')
    #    self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0
    def __init__(self):
        self.image = load_image('life.jpg')
        self.life = 5

    def get_bb(self):
        # fill here
        return self.x - 30, self.y - 25, self.x + 25, self.y + 25

    #def draw(self):
    #    self.image.draw(self.x, self.y)
    #    # fill here for draw
    #    draw_rectangle(*self.get_bb())
    def draw(self):
        #self.image.clip_draw(main_state.penguin.x - main_state.penguin.draw_x, main_state.penguin.y - main_state.penguin.draw_y, 800, 600, 400, 300)
        for i in range(self.life):
            self.image.clip_draw(0, 0, 512, 512, 770 - 50 * i, 570, 50, 50)
            #draw_rectangle(*self.get_bb())

    def update(self):
        #self.y -= self.fall_speed * game_framework.frame_time
        pass
    #fill here for def stop
    def stop(self):
        #self.fall_speed = 0
        pass
