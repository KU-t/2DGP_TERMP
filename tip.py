import random
from pico2d import *
import game_world
import game_framework
import main_state

class Tip:
    image = None

    def __init__(self):
        self.image = load_image('TIP2.png')


    def get_bb(self):
        return self.x - 800, self.y - 600, self.x + 800, self.y + 600

    def draw(self):
        self.image.clip_draw(main_state.penguin.x, main_state.penguin.y, 800, 600, 400, 300)


    def update(self):
        pass

    def stop(self):
        pass
