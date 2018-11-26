from pico2d import *
import game_world
import main_state

class Wall:

    def __init__(self, lx = 400, by = 300, rx = 400, ty = 300):
        self.lx, self.by, self.rx,  self.ty = lx, by, rx, ty
        self.cx, self.cy = 0, 0
        self.exist = True

    def get_bb(self):
        return self.lx - main_state.penguin.x + self.cx - 5, self.by - main_state.penguin.y + self.cy - 5, self.rx - main_state.penguin.x + self.cx + 5, self.ty - main_state.penguin.y + self.cy + 5

    def draw(self):
        draw_rectangle(*self.get_bb())
        #pass

    def draw_move(self):
        pass

    def update(self):
        pass
