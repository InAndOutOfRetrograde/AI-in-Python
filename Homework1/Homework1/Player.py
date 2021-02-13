import pygame

from Agent import Agent
from Vector import Vector

class Player(Agent):

	def __init__(self, position, speed, size, color):
		super().__init__(position, speed, size, color)

	def lineDraw(self,screen):
		super().lineDraw(screen)

	def draw(self, screen):
		super().draw(screen)

	def update(self,player, range):
		super().update(player, range)
		#Movement
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_w] or pressed[pygame.K_UP]: self.vel.VecY -= 5
		if pressed[pygame.K_s] or pressed[pygame.K_DOWN]: self.vel.VecY += 5
		if pressed[pygame.K_a] or pressed[pygame.K_LEFT]: self.vel.VecX -= 5
		if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]: self.vel.VecX += 5

		self.vel = self.vel.normalize().scale(self.spd)
		self.pos += self.vel



