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
        #if event == SPACE:
        #    penguin.fire_ball()

    @staticmethod
    def do(penguin):
        penguin.frame = (penguin.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        #x축 충돌체크
        collision_x = False
        for wall in main_state.walls:
            if main_state.collide_x_wall(penguin, wall):
                collision_x = True
                #penguin.y -= penguin.y_velocity * game_framework.frame_time
        if not collision_x:
            penguin.x += penguin.x_velocity * game_framework.frame_time


        #y축 충돌체크
        collision_y = False
        for wall in main_state.walls:
            if main_state.collide_y_wall(penguin, wall):
                collision_y = True
                #penguin.x -= penguin.x_velocity * game_framework.frame_time
        if not collision_y:
            penguin.y += penguin.y_velocity * game_framework.frame_time


        cx, cy = penguin.x - penguin.bg.window_left, penguin.y - penguin.bg.window_bottom

        #penguin.cx, penguin.cy = cx, cy

#        for life in main_state.lifes:
 #           life.cx, life.cy = cx, cy

  #      for wall in main_state.walls:
   #         wall.cx, wall.cy = cx, cy

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

        draw_rectangle(*penguin.get_bb())
        #draw_rectangle(*penguin.get_collision_bb())

next_state_table = {
    WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
                UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
                UPKEY_M: WalkingState, DOWNKEY_M: WalkingState}
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
        #self.x , self.y = 0, 0
        self.x_velocity, self.y_velocity = 0, 0
        self.frame = 0
        self.direct_frame = 0
        self.event_que = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)
        self.life_count = 0
        self.card_count = 0
        self.shoes_count = 0
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
        if item.type == 'shoes':
            self.shoes_count += 1
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
            self.time_life -= 1


    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.canvas_width//2 - 60 , self.canvas_height//2 + 50 , '(%4d, %4d)' % (self.x, self.y), (0, 0, 0))
        self.font.draw(self.canvas_width//2 - 20 , self.canvas_height//2 + 70 , 'life[%3d]' % self.life_count, (0, 0, 0))
        self.font.draw(self.canvas_width//2 - 20 , self.canvas_height//2 + 90 , 'card[%3d]' % self.card_count, (0, 0, 0))
        self.font.draw(self.canvas_width//2 - 20 , self.canvas_height//2 + 110 , 'shoe[%3d]' % self.shoes_count, (0, 0, 0))
        self.font.draw(self.canvas_width//2 - 20 , self.canvas_height//2 + 130 , 'time[%3d]' % self.time_life, (0, 0, 0))


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