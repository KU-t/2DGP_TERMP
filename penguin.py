from pico2d import *

open_canvas()
huddle = load_image('huddle.png')
TIP = load_image('TIP.png')
penguin = load_image('penguin.png')
frame = 0
frame2 = 0
frame3 = 0
move = 0
move2 = 0
while True:
    clear_canvas()
    TIP.clip_draw(0,0,600,450,400,300,800,600)
    #walking sprite
    penguin.clip_draw(frame * 35, (move + 0) * 47 + 35, 35, 45, 100, 500 - (45 * (move + 0)))
    penguin.clip_draw(frame * 35, (move + 1) * 47 + 35, 35, 45, 100, 500 - (45 * (move + 1)))
    penguin.clip_draw(frame * 35, (move + 2) * 47 + 35, 35, 45, 100, 500 - (45 * (move + 2)))
    penguin.clip_draw(frame * 35, (move + 3) * 47 + 35, 35, 45, 100, 500 - (45 * (move + 3)))
    penguin.clip_draw(frame * 35, (move + 4) * 47 + 35, 35, 45, 100, 500 - (45 * (move + 4)))
    penguin.clip_draw(frame * 35, (move + 5) * 47 + 35, 35, 45, 100 + 5, 500 - (45 * (move + 5)))
    penguin.clip_draw(frame * 35, (move + 6) * 47 + 35, 35, 45, 100 + 6, 500 - (45 * (move + 6)))
    penguin.clip_draw(frame * 35, (move + 7) * 47 + 35, 35, 45, 100 + 5, 500 - (45 * (move + 7)))

    penguin.clip_draw(frame * 35, (move + 0) * 47 + 35, 35, 45, 100 + (45 * (move + 0)), 50 - 2)
    penguin.clip_draw(frame * 35, (move + 1) * 47 + 35, 35, 45, 100 + (35 * (move + 1)), 50)
    penguin.clip_draw(frame * 35, (move + 2) * 47 + 35, 35, 45, 100 + (35 * (move + 2)), 50)
    penguin.clip_draw(frame * 35, (move + 3) * 47 + 35, 35, 45, 100 + (35 * (move + 3)), 50)
    penguin.clip_draw(frame * 35, (move + 4) * 47 + 35, 35, 45, 100 + (35 * (move + 4)), 50 - 4)
    penguin.clip_draw(frame * 35, (move + 5) * 47 + 35, 35, 45, 100 + (35 * (move + 5)), 50 - 7)
    penguin.clip_draw(frame * 35, (move + 6) * 47 + 35, 35, 45, 100 + (35 * (move + 6)), 50 - 7)
    penguin.clip_draw(frame * 35, (move + 7) * 47 + 35, 35, 45, 100 + (35 * (move + 7)), 50 - 4)
    
    
    #sliding sprite
    if frame2 != 2:
        penguin.clip_draw(frame2+1 * 38 + 323, (move + 0) * 47 + 35, 38, 45, 300, 500 - (45 * (move + 0)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 1) * 47 + 35, 38, 45, 300, 500 - (45 * (move + 1)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 2) * 47 + 35, 38, 45, 300, 500 - (45 * (move + 2)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 3) * 47 + 35, 38, 45, 300, 500 - (45 * (move + 3)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 4) * 47 + 35, 38, 45, 300, 500 - (45 * (move + 4)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 5) * 47 + 35, 38, 45, 300 + 5, 500 - (45 * (move + 5)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 6) * 47 + 35, 38, 45, 300 + 6, 500 - (45 * (move + 6)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 7) * 47 + 35, 38, 45, 300 + 5, 500 - (45 * (move + 7)))

        penguin.clip_draw(frame2 * 38 + 323, (move + 0) * 47 + 35, 38, 45, 400 + (45 * (move + 0)), 250 - 2)
        penguin.clip_draw(frame2 * 38 + 323, (move + 1) * 47 + 35, 38, 45, 400 + (35 * (move + 1)), 250)
        penguin.clip_draw(frame2 * 38 + 323, (move + 2) * 47 + 35, 38, 45, 400 + (35 * (move + 2)), 250)
        penguin.clip_draw(frame2 * 38 + 323, (move + 3) * 47 + 35, 38, 45, 400 + (35 * (move + 3)), 250)
        penguin.clip_draw(frame2 * 38 + 323, (move + 4) * 47 + 35, 38, 45, 400 + (35 * (move + 4)), 250 - 4)
        penguin.clip_draw(frame2 * 38 + 323, (move + 5) * 47 + 35, 38, 45, 400 + (35 * (move + 5)), 250 - 7)
        penguin.clip_draw(frame2 * 38 + 323, (move + 6) * 47 + 35, 38, 45, 400 + (35 * (move + 6)), 250 - 7)
        penguin.clip_draw(frame2 * 38 + 323, (move + 7) * 47 + 35, 38, 45, 400 + (35 * (move + 7)), 250 - 4)
        
    else:
        penguin.clip_draw(frame2 * 38 + 323, (move + 0) * 47 + 35, 47, 45, 300, 500 - (45 * (move + 0)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 1) * 47 + 35, 47, 45, 300, 500 - (45 * (move + 1)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 2) * 47 + 35, 47, 45, 300, 500 - (45 * (move + 2)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 3) * 47 + 35, 47, 45, 300, 500 - (45 * (move + 3)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 4) * 47 + 35, 47, 45, 300, 500 - (45 * (move + 4)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 5) * 47 + 35, 47, 45, 300 + 5, 500 - (45 * (move + 5)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 6) * 47 + 35, 47, 45, 300 + 6, 500 - (45 * (move + 6)))
        penguin.clip_draw(frame2 * 38 + 323, (move + 7) * 47 + 35, 47, 45, 300 + 5, 500 - (45 * (move + 7)))

        penguin.clip_draw(frame2 * 38 + 323, (move + 0) * 47 + 35, 47, 45, 400 + (45 * (move + 0)), 250 - 2)
        penguin.clip_draw(frame2 * 38 + 323, (move + 1) * 47 + 35, 47, 45, 400 + (35 * (move + 1)), 250)
        penguin.clip_draw(frame2 * 38 + 323, (move + 2) * 47 + 35, 47, 45, 400 + (35 * (move + 2)), 250)
        penguin.clip_draw(frame2 * 38 + 323, (move + 3) * 47 + 35, 47, 45, 400 + (35 * (move + 3)), 250)
        penguin.clip_draw(frame2 * 38 + 323, (move + 4) * 47 + 35, 47, 45, 400 + (35 * (move + 4)), 250 - 4)
        penguin.clip_draw(frame2 * 38 + 323, (move + 5) * 47 + 35, 47, 45, 400 + (35 * (move + 5)), 250 - 7)
        penguin.clip_draw(frame2 * 38 + 323, (move + 6) * 47 + 35, 47, 45, 400 + (35 * (move + 6)), 250 - 7)
        penguin.clip_draw(frame2 * 38 + 323, (move + 7) * 47 + 35, 47, 45, 400 + (35 * (move + 7)), 250 - 4)
        
    #huddle
    huddle.clip_draw(frame3 * 32, 32 * move2, 32, 32, 400, 300, 48, 48)

    frame = (frame + 1) % 8
    frame2 = (frame2 + 1) % 3
    frame3 = (frame3 + 1) % 3
    update_canvas()
    delay(0.5)
