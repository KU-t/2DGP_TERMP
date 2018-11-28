import random

from pico2d import *
import main_state

class Map:

    def __init__(self):
        self.image = load_image('./image/background.png')
        self.image_penguin_position = load_image('./image/penguin_position.png')
        self.show = True

    def draw(self):
        if self.show:
            self.image.clip_draw(0, 0, 1600, 1200, 675, 100, 200, 150)
            self.image_penguin_position.clip_draw(0, 0, 138, 111, 575 + (main_state.penguin.x / 8), 25 + (main_state.penguin.y / 8), 13, 11)

    def update(self):
        pass

    def handle_event(self, event):
        pass





