import game_framework
import random
from pico2d import *


import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3


class Human:
    image = None
    move_speed = 300

    def __init__(self, x = 400, y = 400, dir = random.randint(0,4), human_type = 'blue_student'):
        self.x, self.y = x, y
        self.velocity_x, self.velocity_y = 0, 0
        self.human_type = human_type
        self.state = 'sleep'
        self.frame = 0
        self.direct = dir
        self.count_change_dir = random.randint(0, 999)
        if not Human.image:
            Human.image = load_image('huddle.png')



    def get_bb(self):
        # fill here
        return self.x - 14, self.y - 25, self.x + 20, self.y + 25


    def fire_ball(self):
        pass


    def add_event(self, event):
        pass

    def update(self):
        self.count_change_dir += 1
        if self.count_change_dir >= 300:
            self.count_change_dir = 0
            self.direct = random.randint(0, 3)

        if self.direct == 1:
            self.velocity_x += 150
        if self.direct == 2:
            self.velocity_x -= 150
        if self.direct == 0:
            self.velocity_y += 150
        if self.direct == 3:
            self.velocity_y -= 150

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += int(self.velocity_x * game_framework.frame_time)
        self.y += int(self.velocity_y * game_framework.frame_time)
        self.velocity_x = 0
        self.velocity_y = 0

    def draw(self):
        if self.human_type == 'red_student':
            Human.image.clip_draw(int(self.frame) * 32 + 32 * 3, 32 * self.direct, 32, 32, self.x, self.y, 48, 48)
        elif self.human_type == 'green_student':
            Human.image.clip_draw(int(self.frame) * 32, 32 * self.direct, 32, 32, self.x, self.y, 48, 48)
        elif self.human_type == 'blue_student':
            Human.image.clip_draw(int(self.frame) * 32 + 32 * 3, 32 * self.direct + 32 * 4, 32, 32, self.x, self.y, 48, 48)
        elif self.human_type == 'resident':
            Human.image.clip_draw(int(self.frame) * 32, 32 * self.direct + 32 * 4, 32, 32, self.x, self.y, 48, 48)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
       pass

    def check_move(self):
        if self.direct == 1:
            pass