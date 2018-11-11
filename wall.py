import random
from pico2d import *
from penguin import Penguin
import game_world
import game_framework
import main_state

# Boy Run Speed

class Wall:

    image = None
    move_speed = 300
    #move_speed = penguin.move_speed
    #def __init__(self):
    #    if Tip.image == None:
    #        Tip.image = load_image('ball21x21.png')
    #    self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0
    def __init__(self, sx = 400, sy = 300, ex = 500, ey = 400):
        self.sx, self.sy = sx, sy
        self.ex, self.ey = ex, ey
        self.velocity_x, self.velocity_y = 0, 0
        self.draw_x, self.draw_y = 0, 0
        self.exist = True
        self.font = load_font('ENCR10B.TTF', 16)



    def get_bb(self):
        # fill here
        return self.sx - self.draw_x - 5, self.sy - self.draw_y - 5, self.ex - self.draw_x + 5, self.ey - self.draw_y + 5

    #def draw(self):
    #    self.image.draw(self.x, self.y)
    #    # fill here for draw
    #    draw_rectangle(*self.get_bb())
    def draw(self):
        if self.exist:
            draw_rectangle(*self.get_bb())
            #self.font.draw(self.sx - self.draw_x, self.sy - self.draw_y + 10, '(x,: %3.2f)' % self.sx, (0, 0, 0))
            #self.font.draw(self.sx - self.draw_x, self.sy - self.draw_y - 10, '(y,: %3.2f)' % self.sy, (0, 0, 0))

    def update(self):
        #self.y -= self.fall_speed * game_framework.frame_time
        self.draw_x -= int(self.velocity_x * game_framework.frame_time)
        self.draw_y -= int(self.velocity_y * game_framework.frame_time)
        self.velocity_x = 0
        self.velocity_y = 0

    #fill here for def stop
    def stop(self):
        #self.fall_speed = 0
        pass
