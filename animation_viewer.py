from pico2d import *
def y_cange(y):
    return 498 - y
open_canvas()

character = load_image('animation.png')

def work():
    pass
def run():
    for i in range(5):
        for frame in range(6):
            clear_canvas()
            character.clip_draw(20+frame * 80, y_cange(280), 60,60, 400, 300,200,200)
            update_canvas()
            delay(0.1)
    delay(1.0)
    pass
def jump():
    for i in range(5):
        x = 100
        for frame in range(6):
            clear_canvas()
            character.clip_draw(20+frame * 80, y_cange(385), 60,60, x, 300,200,200)
            x += 100
            update_canvas()
            delay(0.1)
    delay(1.0)
    pass
def hit():
    for i in range(5):
        for frame in range(3):
            clear_canvas()
            character.clip_draw(20+frame * 80, y_cange(465), 60,60, 400, 300,200,200)
            update_canvas()
            delay(0.1)
    delay(1.0)
    pass

while True:
    work()
    run()
    jump()
    hit()

close_canvas()