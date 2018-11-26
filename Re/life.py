from pico2d import *
import game_world
import main_state

class Life:
    image = None

    def __init__(self, x = 400, y = 300):
        if Life.image == None:
            Life.image = load_image('life.jpg')
        self.x, self.y = x, y
        self.cx, self.cy = 0, 0
        self.exist = True

    def get_bb(self):
        return self.x - main_state.penguin.x + self.cx - 20, self.y - main_state.penguin.y + self.cy - 20, self.x - main_state.penguin.x + self.cx + 20, self.y - main_state.penguin.y + self.cy + 20

    def draw(self):
        if self.exist:
            self.image.draw(self.x - main_state.penguin.x + self.cx, self.y - main_state.penguin.y + self.cy)

    def draw_move(self):
        pass

    def update(self):
        pass
