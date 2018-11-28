import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import main_state

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


animation_names = ['Attack', 'Dead', 'Idle', 'Walk']


class Human:
    images = None

    def load_images(self):
        if Human.images == None:
            Human.images = {}
            for name in animation_names:
                Human.images[name] = [load_image("./zombiefiles/female/"+ name + " (%d)" % i + ".png") for i in range(1, 11)]


    def __init__(self, x, y):
        self.x, self.y = x, y
        self.load_images()
        self.dir = random.random()*2*math.pi # random moving direction
        self.speed = 0
        self.x_velocity, self.y_velocity = 0, 0
        self.cx, self.cy = 0, 0
        self.timer = 1.0 # change direction every 1 sec when wandering
        self.frame = 0
        self.build_behavior_tree()

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random() * 2 * math.pi

    def find_player(self):
        penguin = main_state.get_penguin()
        distance = (penguin.x - self.x) ** 2 + (penguin.y - self.y) ** 2
        if distance < (PIXEL_PER_METER * 5) ** 2:
            self.dir = math.atan2(penguin.y - self.y, penguin.x - self.x)
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL

    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        wander_node = LeafNode("Wander", self.wander)
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node)
        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_children(chase_node, wander_node)
        self.bt = BehaviorTree(wander_chase_node)


    def get_bb(self):
        return self.x - main_state.penguin.x + self.cx - 5, self.y - main_state.penguin.y + self.cy - 5, self.x - main_state.penguin.x + self.cx + 5, self.y - main_state.penguin.y + self.cy + 5

    def get_collision_x_bb(self):
        l, b, r, t = self.get_bb()
        l = l + self.x_velocity * math.cos(self.dir) * game_framework.frame_time
        r = r + self.x_velocity * math.cos(self.dir) * game_framework.frame_time
        return l, b, r, t

    def get_collision_y_bb(self):
        l, b, r, t = self.get_bb()
        b = b + self.y_velocity * math.sin(self.dir)* game_framework.frame_time
        t = t + self.y_velocity * math.sin(self.dir)* game_framework.frame_time
        return l, b, r, t

    def update(self):
        self.bt.run()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x_velocity, self.y_velocity = self.speed, self.speed

        collision_x = False
        for wall in main_state.walls:
            if main_state.collide_x_wall(self, wall):
                collision_x = True
                # penguin.y -= penguin.y_velocity * game_framework.frame_time
        if not collision_x:
            self.x += self.x_velocity * math.cos(self.dir) * game_framework.frame_time

        # y축 충돌체크
        collision_y = False
        for wall in main_state.walls:
            if main_state.collide_y_wall(self, wall):
                collision_y = True
                # penguin.x -= penguin.x_velocity * game_framework.frame_time
        if not collision_y:
            self.y += self.y_velocity * math.sin(self.dir) * game_framework.frame_time

        #self.x += self.x_velocity * math.cos(self.dir) * game_framework.frame_time
        #self.y += self.y_velocity * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(0, self.x, main_state.penguin.bg.w)
        self.y = clamp(0, self.y, main_state.penguin.bg.h)



    def draw(self):

        #self.image.draw(self.x - main_state.penguin.x + self.cx, self.y - main_state.penguin.y + self.cy)

        if math.cos(self.dir) < 0:
            if self.speed == 0:
                pass
                Human.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x - main_state.penguin.x + self.cx, self.y - main_state.penguin.y + self.cy, 50, 50)
            else:
                Human.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x - main_state.penguin.x + self.cx, self.y - main_state.penguin.y + self.cy, 50, 50)
        else:
            if self.speed == 0:
                pass
                Human.images['Idle'][int(self.frame)].draw(self.x - main_state.penguin.x + self.cx, self.y - main_state.penguin.y + self.cy, 50, 50)
            else:
                Human.images['Walk'][int(self.frame)].draw(self.x - main_state.penguin.x  + self.cx, self.y - main_state.penguin.y + self.cy, 50, 50)
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_collision_x_bb())
        draw_rectangle(*self.get_collision_y_bb())

    def handle_event(self, event):
        pass

