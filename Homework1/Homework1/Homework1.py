import pygame
import random

from Player import Player
from Enemy import Enemy
from Sheep import Sheep
from Dog import Dog
from EnemyHunter import EnemyHunter

from Vector import Vector
from Constants import Constants

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False

dogSurface = pygame.image.load('collie.png')
sheepSurface = pygame.image.load('sheep.png')

#player = Player(Constants.POSITION,Constants.PLAYER_SPEED, Constants.SIZE, Constants.COLOR)
dog = Dog(Constants.POSITION,Constants.PLAYER_MAX_SPEED, Constants.GET_SIZE, Constants.COLOR, dogSurface)

#enemy_list = []
sheep_list = []
#enemy_hunter_list = []
for x in range(Constants.SHEEP_AMOUNT):
	#enemy = Enemy(Constants.ENEMY_POSITION + Vector(x*30, Constants.ENEMY_POSITION.VecY),Constants.ENEMY_SPEED, Constants.SIZE, Constants.ENEMY_COLOR, Constants.MAXTIME)
	#enemyHunter = EnemyHunter(Constants.ENEMYHUNTER_POSITION + Vector(x*30, Constants.ENEMYHUNTER_POSITION.VecY), Constants.ENEMYHUNTER_SPEED, Constants.SIZE, Constants.ENEMYHUNTER_COLOR, Constants.MAXTIME)
	sheep = Sheep(Vector(random.uniform(32,Constants.WORLD_WIDTH-32), random.uniform(32, Constants.WORLD_HEIGHT-32)),Constants.SHEEP_MAX_SPEED, Constants.GET_SIZE, Constants.SHEEP_COLOR, Constants.MAXTIME, sheepSurface)
	sheep_list.append(sheep)
	#enemy_list.append(enemy)
	#enemy_hunter_list.append(enemyHunter)

clock = pygame.time.Clock()

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
		if event.type == pygame.QUIT:
			done = True
		

	#cant inherit on player without these parameters???
	#player.update(player, Constants.ENEMY_RANGE)
	dog.update(dog, Constants.ENEMY_RANGE)

	for x in range(len(sheep_list)):
		#enemy_list[x].update(player, Constants.ENEMY_RANGE)
		sheep_list[x].update(dog, Constants.ENEMY_RANGE, sheep_list)
		#enemy_hunter_list[x].update(player, Constants.ENEMYHUNTER_RANGE)
	
	screen.fill((Constants.BACKGROUND_COLOR))
	#player.draw(screen)
	dog.draw(screen)
	
	for x in range(len(sheep_list)):
		#enemy_list[x].draw(screen)
		#enemy_hunter_list[x].draw(screen)
		sheep_list[x].draw(screen, sheep_list)

	pygame.display.flip()
	clock.tick(60)
