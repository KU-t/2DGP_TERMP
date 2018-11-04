import game_framework
from pico2d import *


import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Penguin:

    def __init__(self):
        self.x, self.y, self.move_frame, self.direct_frame = 400, 600, 0, 0
        self.draw_x, self.draw_y = 400, 300
        self.image = load_image('penguin.png')
        self.direction = [False, False, False, False]
        self.move_speed = 10
        self.life = 3
        self.state = 'move'
        #self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.font = load_font('ENCR10B.TTF', 16)
        self.velocity = 0



    def get_bb(self):
        # fill here
        return self.draw_x - 16, self.draw_y - 20, self.draw_x + 16, self.draw_y + 16


    def fire_ball(self):
        pass


    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        self.move_frame = (self.move_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if self.direct_frame == 0:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x, self.draw_y - 2)
        elif self.direct_frame == 4:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 34, 45, self.draw_x + 2, self.draw_y - 4)
        elif self.direct_frame == 5:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 34, 45, self.draw_x + 5, self.draw_y - 7)
        elif self.direct_frame == 6:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x + 6, self.draw_y - 7)
        elif self.direct_frame == 7:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x + 5, self.draw_y - 4)
        else:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x, self.draw_y)

        self.font.draw(self.draw_x - 50, self.draw_y + 60, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #fill here
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
       pass

