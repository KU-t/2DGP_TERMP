import game_framework
from pico2d import *

import game_world
import main_state
from item import Item

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
RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, UPKEY_UP, DOWNKEY_UP, UPKEY_M, DOWNKEY_M = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHTKEY_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFTKEY_UP,
    (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
    (SDL_KEYUP, SDLK_m): UPKEY_M,
    (SDL_KEYDOWN, SDLK_m): DOWNKEY_M
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

        if event == DOWNKEY_M:
            if main_state.map.show:
                main_state.map.show = False
            elif not main_state.map.show:
                main_state.map.show = True
        elif event == UPKEY_M:
            pass

    @staticmethod
    def exit(penguin, event):
        pass

    @staticmethod
    def do(penguin):
        penguin.frame = (penguin.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        #x축 충돌체크
        collision_x = False
        for wall in main_state.walls:
            if main_state.collide_x_wall(penguin, wall):
                collision_x = True
        if not collision_x:
            penguin.x += penguin.x_velocity * game_framework.frame_time

        #y축 충돌체크
        collision_y = False
        for wall in main_state.walls:
            if main_state.collide_y_wall(penguin, wall):
                collision_y = True
        if not collision_y:
            penguin.y += penguin.y_velocity * game_framework.frame_time

        cx, cy = penguin.x - penguin.bg.window_left, penguin.y - penguin.bg.window_bottom

        for game_object in game_world.all_objects():
            game_object.cx, game_object.cy = cx, cy

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
        if not penguin.time_life == 0:
            if penguin.time_life // 100 == 2:
                penguin.image_count_3.draw(penguin.x - main_state.penguin.x + penguin.cx, penguin.y - main_state.penguin.y + penguin.cy + 30)
            if penguin.time_life // 100 == 1:
                penguin.image_count_2.draw(penguin.x - main_state.penguin.x + penguin.cx, penguin.y - main_state.penguin.y + penguin.cy + 30)
            if penguin.time_life // 100 == 0:
                penguin.image_count_1.draw(penguin.x - main_state.penguin.x + penguin.cx, penguin.y - main_state.penguin.y + penguin.cy + 30)


next_state_table = {
    WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
                UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
                UPKEY_M: WalkingState, DOWNKEY_M: WalkingState}
}


class Penguin:
    image = None
    image_count_1 = None
    image_count_2 = None
    image_count_3 = None
    image_wind = None

    def __init__(self, x = 400, y = 300):
        if Penguin.image_count_1 == None:
            Penguin.image = load_image('./image/penguin.png')
            Penguin.image_count_1 = load_image('./image/1.png')
            Penguin.image_count_2 = load_image('./image/2.png')
            Penguin.image_count_3 = load_image('./image/3.png')
            Penguin.image_wind = load_image('./image/wind.png')

        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        # Penguin is only once created, so instance image loading is fine

        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.direction = [False, False, False, False]
        self.x, self.y = x, y
        self.x_velocity, self.y_velocity = 0, 0
        self.frame = 0
        self.direct_frame = 0
        self.event_que = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)
        self.life_count = 3
        self.card_count = 0
        self.skill_count = 0
        self.cx, self.cy = 0, 0
        self.eat_sound = load_wav('pickup.wav')
        self.eat_sound.set_volume(32)
        self.time_life = 0

    def get_bb(self):
        return self.cx - 10, self.cy - 20, self.cx + 10, self.cy + 10

    def get_collision_x_bb(self):
        x = self.x + self.x_velocity * game_framework.frame_time

        cx = x - self.bg.window_left
        return cx - 10, self.cy - 20, cx + 10, self.cy + 10

    def get_collision_y_bb(self):
        y = self.y + self.y_velocity * game_framework.frame_time

        cy = y - self.bg.window_bottom
        return self.cx - 10, cy - 20, self.cx + 10, cy + 10

    def eat(self, item):
        self.eat_sound.play()
        if item.type == 'life':
            self.life_count += 1
        if item.type == 'card':
            self.card_count += 1
        if item.type == 'skill':
            self.skill_count += 1
            self.time_life = 300
        item.exist = False

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w * 4 / 5
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
        if self.time_life > 0:
            self.time_life -= 3

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(750, 580, 'x %2d' % self.life_count, (0, 0, 0))
        Item.image_life.draw(720, 580)
        self.font.draw(750, 550, 'x %2d' % self.card_count, (0, 0, 0))
        Item.image_card.draw(720, 550)

    def draw_victory(self, speed_frame, i):
        self.image.clip_draw((self.frame // 50) * 38 + 323, speed_frame * 47 + 35, 38, 45, self.x, self.y)

        if i:
            self.font.draw(self.x - 40, self.y + 30, 'Thanks!', (100, 100, 255))
        else:
            self.font.draw(self.x - 20, self.y + 30, 'Help!', (100, 100, 255))

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