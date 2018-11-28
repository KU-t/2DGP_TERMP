import random

from pico2d import *


class Map:

    def __init__(self):
        self.image = load_image('background.png')
        self.show = False

    def draw(self):
        if self.show:
            self.image.clip_draw(0, 0, 1600, 1200, 675, 100, 200, 150)


    def update(self):
        pass

    def handle_event(self, event):
        pass





