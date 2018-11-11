import game_framework
import random
from pico2d import *
import main_state

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

    def __init__(self, draw_x = 400, draw_y = 400, dir = random.randint(0,4), human_type = 'blue_student'):
        self.x, self.y = draw_x, draw_y + 300
        self.draw_x, self.draw_y = draw_x, draw_y
        self.velocity_x, self.velocity_y = 0, 0
        self.velocity_draw_x, self.velocity_draw_y = 0, 0
        self.human_type = human_type
        self.state = 'sleep'
        self.frame = 0
        self.direct = dir
        self.count_change_dir = random.randint(0, 999)
        self.state = 'move'
        self.font = load_font('ENCR10B.TTF', 16)
        if not Human.image:
            Human.image = load_image('huddle.png')



    def get_bb(self):
        # fill here
        return self.draw_x - 14, self.draw_y - 25, self.draw_x + 20, self.draw_y + 25


    def fire_ball(self):
        pass


    def add_event(self, event):
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        if self.state == 'move':
            self.count_change_dir += 1
            if self.count_change_dir >= 300:
                self.count_change_dir = 0
                self.direct = random.randint(0, 3)

            if self.direct == 1:
                self.velocity_draw_x += self.move_speed
                self.velocity_x += self.move_speed

            if self.direct == 2:
                self.velocity_draw_x -= self.move_speed
                self.velocity_x -= self.move_speed

            if self.direct == 0:
                self.velocity_draw_y += self.move_speed
                self.velocity_y += self.move_speed

            if self.direct == 3:
                self.velocity_draw_y -= self.move_speed
                self.velocity_y -= self.move_speed

        if self.state == 'follow':
            if self.x > main_state.penguin.x and self.y > main_state.penguin.y:
                self.direct = 2
            elif self.x > main_state.penguin.x and self.y < main_state.penguin.y:
                self.direct = 0
            elif self.x < main_state.penguin.x and self.y > main_state.penguin.y:
                self.direct = 3
            elif self.x < main_state.penguin.x and self.y < main_state.penguin.y:
                self.direct = 1

            self.velocity_draw_x -= (self.x - main_state.penguin.x)
            self.velocity_draw_y -= (self.y - main_state.penguin.y)
            self.velocity_x -= (self.x - main_state.penguin.x)
            self.velocity_y -= (self.y - main_state.penguin.y)


        self.draw_x += int(self.velocity_draw_x * game_framework.frame_time)
        self.draw_y += int(self.velocity_draw_y * game_framework.frame_time)
        self.x += int(self.velocity_x * game_framework.frame_time)
        self.y += int(self.velocity_y * game_framework.frame_time)
        self.velocity_draw_x = 0
        self.velocity_draw_y = 0
        self.velocity_x = 0
        self.velocity_y = 0

    def draw(self):
        if self.human_type == 'red_student':
            Human.image.clip_draw(int(self.frame) * 32 + 32 * 3, 32 * self.direct, 32, 32, self.draw_x, self.draw_y, 48, 48)
        elif self.human_type == 'green_student':
            Human.image.clip_draw(int(self.frame) * 32, 32 * self.direct, 32, 32, self.draw_x, self.draw_y, 48, 48)
        elif self.human_type == 'blue_student':
            Human.image.clip_draw(int(self.frame) * 32 + 32 * 3, 32 * self.direct + 32 * 4, 32, 32, self.draw_x, self.draw_y, 48, 48)
        elif self.human_type == 'resident':
            Human.image.clip_draw(int(self.frame) * 32, 32 * self.direct + 32 * 4, 32, 32, self.draw_x, self.draw_y, 48, 48)

        draw_rectangle(*self.get_bb())
        #self.font.draw(self.draw_x + 10, self.draw_y + 10, '(x,: %3.2f)' % self.x, (0, 0, 0))
        #self.font.draw(self.draw_x + 10, self.draw_y - 10, '(y,: %3.2f)' % self.y, (0, 0, 0))

    def handle_event(self, event):
       pass

    def check_move(self):
        if self.direct == 1:
            pass