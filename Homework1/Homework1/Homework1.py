import pygame
import random

from Agent import Agent
from Player import Player
from Enemy import Enemy
from Sheep import Sheep
from Dog import Dog
from EnemyHunter import EnemyHunter

from Vector import Vector
from Graph import Graph
from Node import Node

import Constants

#################################################################################
# Helper Functions
#################################################################################

def buildGates(graph):
	X = 0
	Y = 1
	# Add the gates to the game
	# pick one end, then pick the second end about 50 spaces away (pick a direction, generate the far end
	for gate in Constants.GATES:
		graph.placeObstacle(Vector(gate[0][X], gate[0][Y]), (0, 255, 0))
		graph.placeObstacle(Vector(gate[1][X], gate[1][Y]), (255, 0, 0))
		print("Placing Obstacles: " + str(gate[0]) + " " + str(gate[1]))

	# Add the final pen based on the final gate
	finalGate = gate[-2:]
	# If the gate is horizontally arranged
	if finalGate[0][Y] == finalGate[1][Y]:
		# If the green gate (the first gate) is on the right, paddock goes "up"
		if finalGate[0][X] > finalGate[1][X]:
			direction = -1
		else:
			direction = 1
		for y in range(finalGate[0][Y] + direction * 16, finalGate[0][Y] + direction * 112, direction * 16):
			graph.placeObstacle(Vector(finalGate[0][X], y), (0, 0, 0))
			graph.placeObstacle(Vector(finalGate[1][X], y), (0, 0, 0))
		for x in range(finalGate[0][X] + direction * 16, finalGate[1][X], direction * 16):
			graph.placeObstacle(Vector(x, finalGate[0][Y] + direction * 96), (0, 0, 0))
	# If the gate is vertically arranged
	else:
		# If the green gate (the first gate) is on the bottom, paddock goes "right"
		if finalGate[0][Y] < finalGate[1][Y]:
			direction = -1
		else:
			direction = 1
		for x in range(finalGate[0][X] + direction * 16, finalGate[1][X] + direction * 112, direction * 16):
			graph.placeObstacle(Vector(x, finalGate[0][Y]), (0, 0, 0))
			graph.placeObstacle(Vector(x, finalGate[1][Y]), (0, 0, 0))
		for y in range(finalGate[0][Y] - direction *  16, finalGate[1][Y], - direction * 16):
			graph.placeObstacle(Vector(finalGate[0][X] + direction * 96, y), (0, 0, 0))

def buildObstacles(graph):
	# Random Obstacles
	for i in range(Constants.NBR_RANDOM_OBSTACLES):
		start = Vector(random.randrange(0, Constants.WORLD_WIDTH), random.randrange(0, Constants.WORLD_HEIGHT))
		graph.placeObstacle(start, (0, 0, 0))
		for j in range(random.randrange(Constants.NBR_RANDOM_OBSTACLES)):
			start += Vector((random.randrange(3) - 1) * Constants.GRID_SIZE, (random.randrange(3) - 1) * Constants.GRID_SIZE)
			while(start.x >= Constants.WORLD_WIDTH - Constants.GRID_SIZE or start.y >= Constants.WORLD_HEIGHT - Constants.GRID_SIZE):
				start += Vector((random.randrange(3) - 1) * Constants.GRID_SIZE, (random.randrange(3) - 1) * Constants.GRID_SIZE)
			graph.placeObstacle(start, (0, 0, 0))

#################################################################################
# Main Functionality
#################################################################################
pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
bounds = Vector(Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT)

#int to make pathfinding slower.
patienceCounter = 0

dogImage = pygame.image.load('collie.png')
sheepImage = pygame.image.load('sheep.png')

#Make the Graph
graph = Graph()

#draw graph/obstacles
buildGates(graph)
buildObstacles(graph)

#Make the Player
dog = Dog(Constants.POSITION,Constants.PLAYER_MAX_SPEED, Constants.GET_SIZE, Constants.COLOR, dogImage)

#Make the Sheep
sheep_list = []
sheep = Sheep(Vector(random.randrange(int(bounds.x * .4), int(bounds.x * .6)),
					 random.randrange(int(bounds.y * .6), int(bounds.y * .8))),
			 Constants.SHEEP_SPEED, Constants.SHEEP_ANGULAR_SPEED, Vector(Constants.DOG_WIDTH, Constants.DOG_HEIGHT), (0, 255, 0), Constants.MAXTIME, sheepImage)
sheep_list.append(sheep)

'''for x in range(Constants.SHEEP_AMOUNT):
	sheep = Sheep(Vector(random.uniform(32,Constants.WORLD_WIDTH-32), random.uniform(32, Constants.WORLD_HEIGHT-32)),Constants.SHEEP_MAX_SPEED, Constants.GET_SIZE, Constants.SHEEP_COLOR, Constants.MAXTIME, sheepSurface)
	sheep_list.append(sheep)
'''
clock = pygame.time.Clock()

done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1: Constants.sheep_vel_line = not Constants.sheep_vel_line; print("sheep vel change")
			if event.key == pygame.K_2: Constants.dog_force_line = not Constants.dog_force_line; print("dog force line change")
			if event.key == pygame.K_3: Constants.bound_force_line = not Constants.bound_force_line; print("bound force line change")
			if event.key == pygame.K_4: Constants.show_neighbors = not Constants.show_neighbors; print("show neighbors change")
			if event.key == pygame.K_5: Constants.bound_box = not Constants.bound_box; print("bound box change")
			if event.key == pygame.K_6: Constants.enable_dog_force = not Constants.enable_dog_force; print("dog force " + str(Constants.enable_dog_force))
			if event.key == pygame.K_7: Constants.enable_align_force = not Constants.enable_align_force; print("align force " + str(Constants.enable_align_force))
			if event.key == pygame.K_8: Constants.enable_seper_force = not Constants.enable_seper_force; print("seper force " + str(Constants.enable_seper_force))
			if event.key == pygame.K_9: Constants.enable_cohes_force = not Constants.enable_cohes_force; print("cohes force " + str(Constants.enable_cohes_force))
			if event.key == pygame.K_0: Constants.enable_bound_force = not Constants.enable_bound_force; print("bound force " + str(Constants.enable_bound_force))
			if event.key == pygame.K_a: Constants.enable_aStar = True; Constants.enable_breadth_first = False; Constants.enable_djikstra = False; Constants.enable_best = False
			if event.key == pygame.K_s: Constants.enable_best =True; Constants.enable_breadth_first = False; Constants.enable_djikstra = False; Constants.enable_aStar = False
			if event.key == pygame.K_d: Constants.enable_djikstra = True; Constants.enable_breadth_first = False; Constants.enable_aStar = False; Constants.enable_best = False
			if event.key == pygame.K_f: Constants.enable_breadth_first = True; Constants.enable_aStar = False; Constants.enable_djikstra = False; Constants.enable_best = False
		if event.type == pygame.QUIT:
			done = True

	# Update agents
	#cant inherit on player without these parameters???
	dog.update(dog, Constants.ENEMY_RANGE)

	for x in range(len(sheep_list)):
		sheep_list[x].update(dog, Constants.ENEMY_RANGE, sheep_list, Constants.GATES)
	
	#pathfinding less than every frame( ideally once every 1/6 of a second)
	patienceCounter += 1
	if(patienceCounter >= 20):
		if(Constants.enable_aStar):
			graph.findPath_AStar(dog.pos,sheep.pos)
		elif(Constants.enable_breadth_first):
			graph.findPath_Breadth(dog.pos, sheep.pos)
		elif(Constants.enable_djikstra):
			graph.findPath_Djikstra(dog.pos, sheep.pos)
		elif(Constants.enable_best):
			graph.findPath_BestFirst(dog.pos, sheep.pos)

		patienceCounter = 0

	# Fill Screen
	screen.fill((Constants.BACKGROUND_COLOR))

	# Redraw Graph
	graph.draw(screen)

	# Draw agents
	dog.draw(screen)

	for x in range(len(sheep_list)):
		sheep_list[x].draw(screen, sheep_list)

	# Double Buffer
	pygame.display.flip()

	# Limit to 60 fps
	clock.tick(60)
