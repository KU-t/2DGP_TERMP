import game_framework
from pico2d import *

import game_world
import main_state


# Penguin Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Penguin Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Penguin Event
RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, UPKEY_UP, DOWNKEY_UP, SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHTKEY_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFTKEY_UP,
    (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Penguin States


class WalkingState:

    @staticmethod
    def enter(penguin, event):
        if event == RIGHTKEY_DOWN:
            penguin.x_velocity += RUN_SPEED_PPS
            penguin.direction[3] = True
        elif event == RIGHTKEY_UP:
            penguin.x_velocity -= RUN_SPEED_PPS
            penguin.direction[3] = False

        if event == LEFTKEY_DOWN:
            penguin.x_velocity -= RUN_SPEED_PPS
            penguin.direction[1] = True
        elif event == LEFTKEY_UP:
            penguin.x_velocity += RUN_SPEED_PPS
            penguin.direction[1] = False

        if event == UPKEY_DOWN:
            penguin.y_velocity += RUN_SPEED_PPS
            penguin.direction[0] = True
        elif event == UPKEY_UP:
            penguin.y_velocity -= RUN_SPEED_PPS
            penguin.direction[0] = False

        if event == DOWNKEY_DOWN:
            penguin.y_velocity -= RUN_SPEED_PPS
            penguin.direction[2] = True
        elif event == DOWNKEY_UP:
            penguin.y_velocity += RUN_SPEED_PPS
            penguin.direction[2] = False


    @staticmethod
    def exit(penguin, event):
        if event == SPACE:
            penguin.fire_ball()

    @staticmethod
    def do(penguin):
        penguin.frame = (penguin.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION


        penguin.x += penguin.x_velocity * game_framework.frame_time
        penguin.y += penguin.y_velocity * game_framework.frame_time

        cx, cy = penguin.x - penguin.bg.window_left, penguin.y - penguin.bg.window_bottom

        penguin.cx, penguin.cy = cx, cy

        for life in main_state.lifes:
            life.cx, life.cy = cx, cy

        for wall in main_state.walls:
            wall.cx, wall.cy = cx, cy

        penguin.x = clamp(0, penguin.x, penguin.bg.w)
        penguin.y = clamp(0, penguin.y, penguin.bg.h)

        Move_Frame_motion(penguin)

    @staticmethod
    def draw(penguin):

        if penguin.direct_frame == 0:
            penguin.image.clip_draw(int(penguin.frame) * 35, penguin.direct_frame * 47 + 35, 35, 45, penguin.cx, penguin.cy - 2)
        elif penguin.direct_frame == 4:
            penguin.image.clip_draw(int(penguin.frame) * 35, penguin.direct_frame * 47 + 35, 34, 45, penguin.cx + 2, penguin.cy - 4)
        elif penguin.direct_frame == 5:
            penguin.image.clip_draw(int(penguin.frame) * 35, penguin.direct_frame * 47 + 35, 34, 45, penguin.cx + 5, penguin.cy - 7)
        elif penguin.direct_frame == 6:
            penguin.image.clip_draw(int(penguin.frame) * 35, penguin.direct_frame * 47 + 35, 35, 45, penguin.cx + 6, penguin.cy - 7)
        elif penguin.direct_frame == 7:
            penguin.image.clip_draw(int(penguin.frame) * 35, penguin.direct_frame * 47 + 35, 35, 45, penguin.cx + 5, penguin.cy - 4)
        else:
            penguin.image.clip_draw(int(penguin.frame) * 35, penguin.direct_frame * 47 + 35, 35, 45, penguin.cx, penguin.cy)

        draw_rectangle(*penguin.get_bb())

next_state_table = {
    WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
                UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
                SPACE: WalkingState}
}


class Penguin:

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        # Penguin is only once created, so instance image loading is fine
        self.image = load_image('penguin.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.direction = [False, False, False, False]
        self.x_velocity, self.y_velocity = 0, 0
        self.frame = 0
        self.direct_frame = 0
        self.event_que = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)
        self.ball_count = 0
        self.cx, self.cy = 0, 0
        self.eat_sound = load_wav('pickup.wav')
        self.eat_sound.set_volume(32)



    def get_bb(self):
        return self.cx - 10, self.cy - 20, self.cx + 10, self.cy + 10

    def eat(self, ball):
        self.eat_sound.play()
        self.ball_count += 1
        ball.exist = False

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.canvas_width//2 - 60, self.canvas_height//2 + 50, '(%4d, %4d)' % (self.x, self.y), (255, 255, 0))
        self.font.draw(self.canvas_width//2 - 20, self.canvas_height//2 + 70, '[%3d]' % self.ball_count, (0, 0, 0))


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)



def Move_Frame_motion(penguin):
    if penguin.direction[0] == True:
        if penguin.direction[1] == True:
            penguin.direct_frame = 4

        elif penguin.direction[2] == True:
            pass

        elif penguin.direction[3] == True:
            penguin.direct_frame = 2

        else:
            penguin.direct_frame = 3

    elif penguin.direction[1] == True:
        if penguin.direction[2] == True:
            penguin.direct_frame = 6

        elif penguin.direction[3] == True:
            pass

        else:
            penguin.direct_frame = 5

    elif penguin.direction[2] == True:
        if penguin.direction[3] == True:
            penguin.direct_frame = 0

        else:
            penguin.direct_frame = 7

    elif penguin.direction[3] == True:
        penguin.direct_frame = 1