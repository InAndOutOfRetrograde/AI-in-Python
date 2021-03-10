import pygame

from Vector import Vector

class Constants:

    FRAME_RATE = 60
    WORLD_WIDTH = 1024
    WORLD_HEIGHT = 768
    BACKGROUND_COLOR = (100, 149, 237)

    POSITION = Vector(370,270)
    WIDTH = float(16)
    HEIGHT = float(32)
    GET_SIZE = Vector(WIDTH, HEIGHT)
    COLOR = (255, 255 ,0)
    PLAYER_MAX_SPEED = 5.5

    SHEEP_POSITION = Vector(150, 150)
    SHEEP_COLOR = (255,0,0)
    SHEEP_MAX_SPEED = 5
    SHEEP_RANGE = 30
    SHEEP_BOUNDARY_FORCE = 1
    DOG_CHASE_FORCE = 1
    HERD_ALIGNMENT_FORCE = 1
    HERD_SEPERATION_FORCE = .4
    HERD_COHESION_FORCE = .2
    SHEEP_BOUNDARY_DISTANCE = 50
    SHEEP_TURN_SPEED = .0000000003
    SHEEP_AMOUNT = 30

    ENEMY_POSITION = Vector(100, 100)
    ENEMY_COLOR = (255,0,0)
    ENEMY_MAX_SPEED = 5
    ENEMY_RANGE = 100

    ENEMYHUNTER_POSITION = Vector(500, 500)
    ENEMYHUNTER_COLOR = (255,0,255)
    ENEMYHUNTER_MAX_SPEED = 1
    ENEMYHUNTER_RANGE = 100

    clock = pygame.time.Clock()
    MAXTIME = 4.0 * clock.tick(60)

    sheep_vel_line     = True # Toggle Sheep Velocity line.
    dog_force_line     = True # Toggle Dog Force line.
    bound_force_line   = True # Toggle Boundary Force lines.
    show_neighbors     = True # Toggle Neighbor lines.
    bound_box          = True # Toggle Bounding Boxes.
    enable_dog_force   = True # Toggle Dog Forces.
    enable_align_force = True # Toggle Alignment Forces.
    enable_seper_force = True # Toggle Separation Forces
    enable_cohes_force = True # Toggle Cohesion Forces.
    enable_bound_force = True # Toggle Boundary Forces.


    