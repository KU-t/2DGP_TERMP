from pico2d import *
import game_world
import main_state

class Wall:
    image = None

    def __init__(self, lx = 400, by = 300, rx = 400, ty = 300, Door = False):
        self.lx, self.by, self.rx,  self.ty = lx, by, rx, ty
        self.cx, self.cy = 0, 0
        self.door = Door
        self.open = False
        if self.image == None:
            self.image = load_image('life.jpg')

    def get_bb(self):
        if self.door:
            if self.open:
                return 0, 0, 0, 0
        return self.lx - main_state.penguin.x + self.cx - 5, self.by - main_state.penguin.y + self.cy - 5, self.rx - main_state.penguin.x + self.cx + 5, self.ty - main_state.penguin.y + self.cy + 5

    def draw(self):
        draw_rectangle(*self.get_bb())
        if self.door:
            if not self.open:
                self.image.draw((self.rx + self.lx)/2 - main_state.penguin.x + self.cx, (self.ty + self.by)/2 - main_state.penguin.y + self.cy)

    def draw_move(self):
        pass

    def update(self):
        pass
