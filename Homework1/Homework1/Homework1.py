import pygame

from Player import Player
from Vector import Vector

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

position = Vector(30,30)
velocity = Vector(30,30)
size = Vector(60,60)
color = (255, 0 ,0)

player = Player(position,velocity,size)

myFont = pygame.font.SysFont("Times New Roman", 18)
clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	player.update()
	
	screen.fill((100, 149, 237))
	player.draw(screen, color)

	pygame.display.flip()
	clock.tick(60)
import pygame

from Player import Player
from Vector import Vector

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

position = Vector(30,30)
velocity = Vector(5,5)
size = Vector(60,60)
color = (255, 0 ,0)
print(position.VecY)
player = Player(position,velocity,size)

myFont = pygame.font.SysFont("Times New Roman", 18)
clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	player.update()
	
	screen.fill((100, 149, 237))
	player.draw(screen, color)

	pygame.display.flip()
	clock.tick(60)
