from pico2d import *
import game_world
import main_state

class Item:
    image_life = None
    image_card = None
    image_shoes = None

    def __init__(self, x, y, type = 'life'):
        if Item.image_life == None:
            Item.image_life = load_image('./image/life.png')
            Item.image_card = load_image('./image/card.png')
            Item.image_skill = load_image('./image/skill.png')

        self.type = type
        self.x, self.y = x, y
        self.cx, self.cy = 0, 0
        self.exist = True
        self.type = type

    def get_bb(self):
        return self.x - main_state.penguin.x + self.cx - 20, self.y - main_state.penguin.y + self.cy - 20, self.x - main_state.penguin.x + self.cx + 20, self.y - main_state.penguin.y + self.cy + 20

    def draw(self):
        if self.exist:
            if self.type == 'life':
                self.image_life.draw(self.x - main_state.penguin.x + self.cx, self.y - main_state.penguin.y + self.cy)
            if self.type == 'card':
                self.image_card.draw(self.x - main_state.penguin.x + self.cx, self.y - main_state.penguin.y + self.cy)
            if self.type == 'skill':
                self.image_skill.clip_draw(0, 0, 600, 600, self.x - main_state.penguin.x + self.cx, self.y - main_state.penguin.y + self.cy, 32, 32)

    def draw_move(self):
        pass

    def update(self):
        pass
