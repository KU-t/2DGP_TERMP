from pico2d import *

open_canvas()
huddle = load_image('huddle.png')
frame = 0
move = 7

while True:
    clear_canvas()
    huddle.clip_draw(frame * 32 , 32 * move, 32, 32, 400, 300, 64, 64)
    frame = (frame + 1) % 3
    delay(0.25)
    update_canvas()