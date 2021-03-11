import pygame

from Vector import Vector

class Constants:

    FRAME_RATE = 60
    WORLD_WIDTH = 1024
    WORLD_HEIGHT = 768
    BACKGROUND_COLOR = (100, 149, 237)

    #pathfinding setup
    GATE_COUNT = 4
    GATE_WIDTH = 100
    GATES = [ [ [104, 552], [104, 664] ], \
	          [ [104, 216], [104, 104] ], \
		      [ [808, 616], [696, 616] ], \
		      [ [936, 152], [824, 152] ], \
		      #[ [456, 440], [456, 328] ]  ]		# vertical, green is on bottom (backwards c)
		      #[ [568, 328], [568, 440] ]  ]		# vertical, green is on top (c)
		      [ [456, 328], [568, 328] ]  ]	# horizontal, green on left (u)
		      #[ [568, 440], [456, 440] ]  ]	# horizontal, green on right (n)
    NBR_RANDOM_OBSTACLES = 20

    POSITION = Vector(370,270)
    WIDTH = float(16)
    HEIGHT = float(32)
    GET_SIZE = Vector(WIDTH, HEIGHT)
    COLOR = (255, 255 ,0)
    PLAYER_MAX_SPEED = 3

    SHEEP_COLOR = (255,0,0)
    SHEEP_WIDTH = WIDTH
    SHEEP_HEIGHT = HEIGHT
    SHEEP_SPEED = 5
    SHEEP_ANGULAR_SPEED = .02
    SHEEP_AMOUNT = 30

    DOG_WIDTH = WIDTH
    DOG_HEIGHT = HEIGHT

    SHEEP_NEIGHBOR_RANGE = 30
    SHEEP_BOUNDARY_RANGE = 50
    SHEEP_OBSTACLE_RANGE = 50
    SHEEP_BOUNDARY_FORCE = 0.5
    HERD_DOG_CHASE_FORCE = 0.3
    HERD_ALIGNMENT_FORCE = 1
    HERD_SEPERATION_FORCE = 0.325
    HERD_COHESION_FORCE = 0.3
    SHEEP_OBSTACLE_INFLUENCE_FORCE = 0.3

    MIN_ATTACK_DIST = 100

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
    enable_obst_debug  = False
    enable_dog_force   = True # Toggle Dog Forces.
    enable_align_force = True # Toggle Alignment Forces.
    enable_seper_force = True # Toggle Separation Forces
    enable_cohes_force = True # Toggle Cohesion Forces.
    enable_grid_lines  = False # Toggle Grid Lines
    enable_bound_force = True # Toggle Boundary Forces.

    #Graph Constants
    GRID_SIZE = 16



    