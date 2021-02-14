import pygame

from Player import Player
from Enemy import Enemy
from EnemyHunter import EnemyHunter
from Vector import Vector
from Constants import Constants

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False

player = Player(Constants.POSITION,Constants.SPEED, Constants.SIZE, Constants.COLOR)
enemy = Enemy(Constants.ENEMY_POSITION,Constants.ENEMY_SPEED, Constants.SIZE, Constants.ENEMY_COLOR, Constants.MAXTIME)
enemyHunter = EnemyHunter(Constants.ENEMYHUNTER_POSITION, Constants.ENEMYHUNTER_SPEED, Constants.SIZE, Constants.ENEMYHUNTER_COLOR, Constants.MAXTIME)

clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	#cant inherit on player without these parameters???
	player.update(player, Constants.ENEMY_RANGE)
	enemy.update(player, Constants.ENEMY_RANGE)
	enemyHunter.update(player, Constants.ENEMYHUNTER_RANGE)
	
	screen.fill((Constants.BACKGROUND_COLOR))
	player.draw(screen)
	enemy.draw(screen)
	enemyHunter.draw(screen)

	pygame.display.flip()
	clock.tick(60)
