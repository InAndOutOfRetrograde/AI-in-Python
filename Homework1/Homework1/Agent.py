import pygame

from Vector import Vector

class Agent:

	def __init__(self, position, speed, size, color):
		self.pos = position
		self.spd = speed
		self.vel = Vector(0,0)
		self.siz = size
		self.center = Vector(0,0)
		self.color = color
		self.It = False
		self.rectangle = pygame.Rect(self.pos.VecX, self.pos.VecY, self.siz, self.siz)
		
	def lineDraw(self, screen):
		if self.vel != Vector(0,0):
			self.line_length = self.vel.scale(10)
			pygame.draw.line(screen, (0,0,255), (self.center.VecX, self.center.VecY), (self.center.VecX + self.line_length.VecX, self.center.VecY + self.line_length.VecY), 4)

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rectangle)
		self.lineDraw(screen)

	def update(self, player, range):
		self.vel.VecX = 0
		self.vel.VecY = 0

		self.center = self.pos + Vector((self.siz * 0.5)-1, (self.siz * 0.5)-1)
		self.rectangle = pygame.Rect(self.pos.VecX, self.pos.VecY, self.siz, self.siz)

