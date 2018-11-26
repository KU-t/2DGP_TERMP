from pico2d import *

class Wall:

    def __init__(self):
        self.life = 5

    def get_bb(self):
        # fill here
        return self.x - 30, self.y - 25, self.x + 25, self.y + 25

    def draw(self):

        for i in range(self.life):
            self.image.clip_draw(0, 0, 512, 512, 770 - 50 * i, 570, 50, 50)

    def update(self):
        pass

    def stop(self):
        pass
