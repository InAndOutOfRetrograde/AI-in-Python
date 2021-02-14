import pygame

from Vector import Vector

class Constants:

    FRAME_RATE = 60
    WORLD_WIDTH = 800
    WORLD_HEIGHT = 600
    BACKGROUND_COLOR = (100, 149, 237)

    POSITION = Vector(370,270)
    SIZE = 10
    COLOR = (255, 255 ,0)
    SPEED = 5.5

    ENEMY_POSITION = Vector(100, 100)
    ENEMY_COLOR = (255,0,0)
    ENEMY_SPEED = 5
    ENEMY_RANGE = 100

    ENEMYHUNTER_POSITION = Vector(500, 500)
    ENEMYHUNTER_COLOR = (255,0,255)
    ENEMYHUNTER_SPEED = 5
    ENEMYHUNTER_RANGE = 100

    clock = pygame.time.Clock()
    MAXTIME = 4.0 * clock.tick(60)


    