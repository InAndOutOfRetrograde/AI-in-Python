import pygame

from Agent import Agent
from Vector import Vector

class Player(Agent):

	def __init__(self, position, speed, size, color, surface):
		super().__init__(position, speed, size, color, surface)

	def lineDraw(self,screen):
		super().lineDraw(screen)

	def draw(self, screen):
		super().draw(screen)
		
	def update(self,player, range):
		super().update(player, range)
		#Movement

		self.vel = Vector(0,0)
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_w] or pressed[pygame.K_UP]: self.vel.y -= 1
		if pressed[pygame.K_s] or pressed[pygame.K_DOWN]: self.vel.y += 1
		if pressed[pygame.K_a] or pressed[pygame.K_LEFT]: self.vel.x -= 1
		if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]: self.vel.x += 1
		if self.vel.x != 0 or self.vel.y != 0: 
			self.vel = self.vel.normalize().scale(self.maxSpd)
			self.pos += self.vel
		else:
			self.vel = Vector(0,0)

		



