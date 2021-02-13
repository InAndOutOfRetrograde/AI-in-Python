import pygame

from Vector import Vector

class Player:

	def __init__(self, position, velocity, size):
		self.pos = position
		self.vel = velocity
		self.siz = size
		print(position.VecY)
		print(velocity.VecY)
		print(size.VecY)

	def draw(self, screen, color):
		pygame.draw.rect(screen, color, pygame.Rect(self.pos.VecX, self.pos.VecY, 60,60))

	def update(self):
		pressed = pygame.key.get_pressed()
		self.vel.VecX = 0
		self.vel.VecY = 0
		if pressed[pygame.K_w]: self.vel.VecY -= 5
		if pressed[pygame.K_s]: self.vel.VecY += 5
		if pressed[pygame.K_a]: self.vel.VecX -= 5
		if pressed[pygame.K_d]: self.vel.VecX += 5
		self.vel = self.vel.normalize()
		self.pos += self.vel



