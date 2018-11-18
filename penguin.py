import game_framework
from pico2d import *

import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 1)  # 10 pixel 100 cm
RUN_SPEED_KMPH = 18.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Penguin:

    def __init__(self):
        self.x, self.y, self.move_frame, self.direct_frame = 1200 + 60, 600, 0, 0
        self.image = load_image('penguin.png')
        self.direction = [False, False, False, False]
        self.move_speed = 300
        self.time_life = 0
        self.state = 'move'
        self.item = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.velocity_x, self.velocity_y = 0, 0



    def get_bb(self):
        # fill here
        return 400 - 12, 300 - 20, 400 + 12, 300 + 16

    def get_bb_collision_wall(self):
        return 400 + int(self.velocity_x * game_framework.frame_time) - 12, 300 + int(self.velocity_y * game_framework.frame_time) - 20, 400 + int(self.velocity_x * game_framework.frame_time)+ 12, 300 + int(self.velocity_y * game_framework.frame_time)+ 16

    def fire_ball(self):
        pass

    def add_event(self, event):
        pass

    def update(self):
        self.move_frame = (self.move_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        self.x += int(self.velocity_x * game_framework.frame_time)
        self.y += int(self.velocity_y * game_framework.frame_time)

        self.velocity_x = 0
        self.velocity_y = 0

        if self.time_life > 0:
            self.time_life -= 1


    def draw(self):

        if self.direct_frame == 0:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 35, 45, 400, 300 - 2)
        elif self.direct_frame == 4:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 34, 45, 400 + 2, 300 - 4)
        elif self.direct_frame == 5:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 34, 45, 400 + 5, 300 - 7)
        elif self.direct_frame == 6:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 35, 45, 400 + 6, 300 - 7)
        elif self.direct_frame == 7:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 35, 45, 400 + 5, 300 - 4)
        else:
            self.image.clip_draw(int(self.move_frame) * 35, self.direct_frame * 47 + 35, 35, 45, 400, 300)

        #self.font.draw(self.draw_x - 50, self.draw_y + 60, '(Time: %3.2f)' % get_time(), (0, 0, 0))
        #self.font.draw(self.draw_x - 50, self.draw_y + 80, '(life: %3.2f)' % self.time_life, (0, 0, 0))
        #self.font.draw(self.draw_x - 50, self.draw_y + 100, '(item: %3.2f)' % self.item, (0, 0, 0))
        #self.font.draw(self.draw_x - 100, self.draw_y + 120, '(Frametime: %3.2f)' % game_framework.frame_time, (0, 0, 0))
        self.font.draw(self.x - 100, self.y + 160, '(x,: %3.2f)' % self.x , (0, 0, 0))
        self.font.draw(self.x - 100, self.y + 140, '(y,: %3.2f)' % self.y, (0, 0, 0))

        #fill here
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb_collision_wall())

    def handle_event(self, event):
       pass

