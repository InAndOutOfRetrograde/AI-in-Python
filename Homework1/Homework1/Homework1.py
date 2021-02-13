import pygame

from Player import Player
from Enemy import Enemy
from Vector import Vector
from Constants import Constants

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False

player = Player(Constants.POSITION,Constants.SPEED, Constants.SIZE, Constants.COLOR)
enemy = Enemy(Constants.ENEMY_POSITION,Constants.ENEMY_SPEED, Constants.SIZE, Constants.ENEMY_COLOR)

clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	#cant inherit on player without these parameters???
	player.update(player, Constants.ENEMY_RANGE)
	enemy.update(player, Constants.ENEMY_RANGE)
	
	screen.fill((Constants.BACKGROUND_COLOR))
	player.draw(screen)
	enemy.draw(screen)

	pygame.display.flip()
	clock.tick(60)
