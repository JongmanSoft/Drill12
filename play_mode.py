import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy
    global zombies

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    zombies = [Zombie() for _ in  range(5)]
    game_world.add_objects(zombies,1)


    # fill here
    global balls
    balls =[]
    game_world.add_objects(balls, 1)
    game_world.add_collision_pair('boy:ball', boy, None)

    for zombie in zombies:
        game_world.add_collision_pair('zombie:ball', zombie, None)

    #충돌 검사 필요상황을 등록
    for zombie in zombies:
        game_world.add_collision_pair('zombie:boy', zombie, boy)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # for ball in balls.copy(): #remove를 해주기 때문에 카피를 해줌
    #     if game_world.collide(boy, ball):
    #         print("COLLISION boy:ball")
    #         boy.ball_count += 1
    #         game_world.remove_object(ball)
    #         balls.remove(ball)
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

