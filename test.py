from pico2d import *
import random

open_canvas()
TIP = load_image('TIP.png')
Life = load_image('life.jpg')


def handle_events():
    global penguin, running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            penguin.direction[0] = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            penguin.direction[1] = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            penguin.direction[2] = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            penguin.direction[3] = True

        elif event.type == SDL_KEYUP and event.key == SDLK_UP:
            penguin.direction[0] = False
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            penguin.direction[1] = False
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            penguin.direction[2] = False
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            penguin.direction[3] = False


class Penguin:
    global shoes

    def __init__(self):
        self.x, self.y, self.move_frame, self.direct_frame = 400, 600, 0, 0
        self.draw_x, self.draw_y = 400, 300
        self.image = load_image('penguin.png')
        self.direction = [False, False, False, False]
        self.move_speed = 10
        self.life = 3
        self.state = 'move'

    def update(self):
      pass

    def draw(self):
        if self.direct_frame == 0:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x, self.draw_y - 2)
        elif self.direct_frame == 4:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 34, 45, self.draw_x + 2, self.draw_y - 4)
        elif self.direct_frame == 5:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 34, 45, self.draw_x + 5, self.draw_y - 7)
        elif self.direct_frame == 6:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x + 6, self.draw_y - 7)
        elif self.direct_frame == 7:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x + 5, self.draw_y - 4)
        else:
            self.image.clip_draw(self.move_frame * 35, self.direct_frame * 47 + 35, 35, 45, self.draw_x, self.draw_y)

        for i in range(self.life):
            Life.clip_draw(0, 0, 512, 512, 770 - 50 * i, 570, 50, 50)


class Shoes:

    def __init__(self):
        self.x, self.y = 800, 600

    def update(self):
        pass

    def draw(self):
        Life.clip_draw(0, 0, 512, 512, self.x, self.y, 50, 50)


class Human:
    image = None

    def __init__(self, x, y, human_type):
        self.x = x
        self.y = y
        self.human_type = human_type
        self.state = 'sleep'
        self.frame = 0
        self.direct = 0

        if Human.image == None:
            Human.image = load_image('huddle.png')

    def draw(self):
        if self.human_type == 'red_student':
            Human.image.clip_draw(self.frame * 32 + 32 * 3, 32 * self.direct, 32, 32, self.x, self.y, 48, 48)
        elif self.human_type == 'green_student':
            Human.image.clip_draw(self.frame * 32, 32 * self.direct, 32, 32, self.x, self.y, 48, 48)
        elif self.human_type == 'blue_student':
            Human.image.clip_draw(self.frame * 32 + 32 * 3, 32 * self.direct + 32 * 4, 32, 32, self.x, self.y, 48, 48)
        elif self.human_type == 'resident':
            Human.image.clip_draw(self.frame * 32, 32 * self.direct + 32 * 4, 32, 32, self.x, self.y, 48, 48)


class Room:

    def __init__(self, x, y, _type):
        self.x = x
        self.y = y
        self.Left = x - 100
        self.Right = x + 100
        self.Bottom = y - 75
        self.Top = y + 75
        self.state = 'off'
        self.type = _type

    def check_penguin_collision_out(self):
        if penguin.y + penguin.move_speed >= self.Top and penguin.direction[0]:
            penguin.direction[0] = False
        if penguin.x - penguin.move_speed <= self.Left and penguin.direction[1]:
            penguin.direction[1] = False
        if penguin.y - penguin.move_speed <= (self.Bottom + 10) and penguin.direction[2]:
            penguin.direction[2] = False
        if penguin.x + penguin.move_speed >= self.Right and penguin.direction[3]:
            penguin.direction[3] = False

    def check_penguin_collision_in(self):

        if self.Left <= penguin.x and penguin.x <= self.Right:
            if penguin.y + penguin.move_speed == (self.Bottom + 10) and penguin.direction[0]:
                penguin.direction[0] = False
            if penguin.y - penguin.move_speed == (self.Top + 10) and penguin.direction[2]:
                penguin.direction[2] = False

        if (self.Bottom + 10) <= penguin.y and penguin.y <= (self.Top + 10):
            if penguin.x - penguin.move_speed == self.Right and penguin.direction[1]:
                penguin.direction[1] = False
            if penguin.x + penguin.move_speed == self.Left and penguin.direction[3]:
                penguin.direction[3] = False

    def check_human_collision(self):
        pass


def move_obj():
    if penguin.direction[0] == True:
        if penguin.direction[1] == True:
            count_x_decrease()
            count_y_increase()
            penguin.direct_frame = 4

        elif penguin.direction[2] == True:
            pass

        elif penguin.direction[3] == True:
            count_x_increase()
            count_y_increase()
            penguin.direct_frame = 2

        else:
            count_y_increase()
            penguin.direct_frame = 3

    elif penguin.direction[1] == True:
        if penguin.direction[2] == True:
            count_x_decrease()
            count_y_decrease()
            penguin.direct_frame = 6

        elif penguin.direction[3] == True:
            pass

        else:
            count_x_decrease()
            penguin.direct_frame = 5

    elif penguin.direction[2] == True:
        if penguin.direction[3] == True:
            count_x_increase()
            count_y_decrease()
            penguin.direct_frame = 0

        else:
            count_y_decrease()
            penguin.direct_frame = 7

    elif penguin.direction[3] == True:
        count_x_increase()
        penguin.direct_frame = 1


def update_obj():

    penguin.move_frame = (penguin.move_frame + 1) % 8

    for student in students:
        student.frame = (student.frame + 1) % 3
        if student.frame == 0:
            student.direct = random.randrange(0, 4)
    for resident in residents:
        resident.frame = (resident.frame + 1) % 3
        #resident.x += 5;
        if resident.frame == 0:
            resident.direct = random.randrange(0, 4)

    for room in rooms:
        room.check_penguin_collision_in()

    for room in rooms:
        if room.Left < penguin.x and penguin.x < room.Right and room.Bottom < penguin.y and penguin.y < room.Top:
            room.check_penguin_collision_out()
            break

    move_obj()



def count_x_increase():
    if penguin.x >= 1200:
        if penguin.x < 1590:
            penguin.draw_x += penguin.move_speed
            shoes.x += penguin.move_speed
            for student in students:
                student.x += penguin.move_speed
            for resident in residents:
                resident.x += penguin.move_speed

    elif penguin.x < 400:
        if penguin.x >= 10:
            penguin.draw_x += penguin.move_speed
            shoes.x += penguin.move_speed
            for student in students:
                student.x += penguin.move_speed
            for resident in residents:
                resident.x += penguin.move_speed

    if penguin.x < 1590:
        penguin.x += penguin.move_speed
        shoes.x -= penguin.move_speed
        for student in students:
            student.x -= penguin.move_speed
        for resident in residents:
            resident.x -= penguin.move_speed

def count_y_increase():
    if penguin.y >= 900:
        if penguin.y < 1180:
            penguin.draw_y += penguin.move_speed
            shoes.y += penguin.move_speed
            for student in students:
                student.y += penguin.move_speed
            for resident in residents:
                resident.y += penguin.move_speed

    elif penguin.y >= 20:
        if penguin.y < 300:
            penguin.draw_y += penguin.move_speed
            shoes.y += penguin.move_speed
            for student in students:
                student.y += penguin.move_speed
            for resident in residents:
                resident.y += penguin.move_speed

    if penguin.y < 1180:
        penguin.y += penguin.move_speed
        shoes.y -= penguin.move_speed
        for student in students:
            student.y -= penguin.move_speed
        for resident in residents:
           resident.y -= penguin.move_speed


def count_x_decrease():
    if penguin.x <= 400:
        if penguin.x > 10:
            penguin.draw_x -= penguin.move_speed
            shoes.x -= penguin.move_speed
            for student in students:
                student.x -= penguin.move_speed
            for resident in residents:
                resident.x -= penguin.move_speed

    elif penguin.x > 1200:
        if penguin.x <= 1590:
            penguin.draw_x -= penguin.move_speed
            shoes.x -= penguin.move_speed
            for student in students:
                student.x -= penguin.move_speed
            for resident in residents:
                resident.x -= penguin.move_speed

    if penguin.x > 10:
        penguin.x -= penguin.move_speed
        shoes.x += penguin.move_speed
        for student in students:
            student.x += penguin.move_speed
        for resident in residents:
               resident.x += penguin.move_speed

def count_y_decrease():
    if penguin.y > 900:
        if penguin.y <= 1180:
            penguin.draw_y -= penguin.move_speed
            shoes.y -= penguin.move_speed
            for student in students:
                student.y -= penguin.move_speed
            for resident in residents:
                resident.y -= penguin.move_speed

    elif penguin.y > 20:
        if penguin.y <= 300:
            penguin.draw_y -= penguin.move_speed
            shoes.y -= penguin.move_speed
            for student in students:
                student.y -= penguin.move_speed
            for resident in residents:
                resident.y -= penguin.move_speed

    if penguin.y > 20:
        penguin.y -= penguin.move_speed
        shoes.y += penguin.move_speed
        for student in students:
            student.y += penguin.move_speed
        for resident in residents:
            resident.y += penguin.move_speed


shoes = Shoes()
penguin = Penguin()

students = [Human(40, 300, 'red_student'), Human(80, 300, 'green_student'), Human(120, 300, 'blue_student')]

residents = [Human(300, 200, 'resident')]

rooms = [Room(200 * 1 + 100, 150 * 1 + 75, 0)]

running = True
Object = [shoes, penguin]


while running:
    handle_events()
    update_obj()

    clear_canvas()
    TIP.clip_draw(penguin.x - penguin.draw_x, penguin.y - penguin.draw_y, 800, 600, 400, 300)
    shoes.draw()
    penguin.draw()

    for student in students:
        student.draw()

    for resident in residents:
        resident.draw()

    update_canvas()

    delay(0.1)

close_canvas()