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

enemy_list = []
enemy_hunter_list = []
for x in range(6):
	enemy = Enemy(Constants.ENEMY_POSITION + Vector(x*30, Constants.ENEMY_POSITION.VecY),Constants.ENEMY_SPEED, Constants.SIZE, Constants.ENEMY_COLOR, Constants.MAXTIME)
	enemyHunter = EnemyHunter(Constants.ENEMYHUNTER_POSITION + Vector(x*30, Constants.ENEMYHUNTER_POSITION.VecY), Constants.ENEMYHUNTER_SPEED, Constants.SIZE, Constants.ENEMYHUNTER_COLOR, Constants.MAXTIME)
	enemy_list.append(enemy)
	enemy_hunter_list.append(enemyHunter)

clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	#cant inherit on player without these parameters???
	player.update(player, Constants.ENEMY_RANGE)
	for x in range(6):
		enemy_list[x].update(player, Constants.ENEMY_RANGE)
		enemy_hunter_list[x].update(player, Constants.ENEMYHUNTER_RANGE)
	
	screen.fill((Constants.BACKGROUND_COLOR))
	player.draw(screen)
	
	for x in range(6):
		enemy_list[x].draw(screen)
		enemy_hunter_list[x].draw(screen)

	pygame.display.flip()
	clock.tick(60)
