import random
from pico2d import *
from penguin import Penguin
import game_world
import game_framework
import main_state

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 1)  # 10 pixel 100 cm
RUN_SPEED_KMPH = 18.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Shoe:

    image = None
    move_speed = 300
    #move_speed = penguin.move_speed
    #def __init__(self):
    #    if Tip.image == None:
    #        Tip.image = load_image('ball21x21.png')
    #    self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0
    def __init__(self, x = 400, y = 300):
        self.x, self.y = x, y
        self.velocity_x, self.velocity_y = 0, 0
        self.draw_x, self.draw_y = 0, 0
        self.exist = True
        self.font = load_font('ENCR10B.TTF', 16)
        if Shoe.image == None:
            Shoe.image = load_image('life.jpg')


    def get_bb(self):
        # fill here
        return self.x - self.draw_x - 17, self.y - self.draw_y - 16, self.x  - self.draw_x + 16, self.y - self.draw_y + 14

    #def draw(self):
    #    self.image.draw(self.x, self.y)
    #    # fill here for draw
    #    draw_rectangle(*self.get_bb())
    def draw(self):
        if self.exist:
            self.image.clip_draw(0, 0, 512, 512, self.x - self.draw_x, self.y - self.draw_y, 50, 50)
            draw_rectangle(*self.get_bb())
            self.font.draw(self.x - self.draw_x, self.y - self.draw_y + 10, '(x,: %3.2f)' % self.x, (0, 0, 0))
            self.font.draw(self.x - self.draw_x, self.y - self.draw_y - 10, '(y,: %3.2f)' % self.y, (0, 0, 0))

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
