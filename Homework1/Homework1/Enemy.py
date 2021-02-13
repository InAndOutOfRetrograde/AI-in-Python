import pygame

from Agent import Agent
from Vector import Vector

class Enemy(Agent):

	def __init__(self, position, speed, size, color):
		super().__init__(position, speed, size, color)
		self.vecToPlayer = Vector(0,0)
		self.currLineColor = (0,0,255)
		self.It = True;

	def draw(self, screen):
		super().draw(screen)
		
	def lineDraw(self,screen):
		if self.vel != Vector(0,0) :
			self.line_length = self.vel.scale(10)
			pygame.draw.line(screen, self.currLineColor, (self.center.VecX, self.center.VecY), (self.center.VecX + self.line_length.VecX, self.center.VecY + self.line_length.VecY), 4)

	def seek(self):
		self.vel = self.vecToPlayer
		self.vel = self.vel.normalize().scale(self.spd)
		self.pos += self.vel

	def flee(self):
		self.vel = self.vecToPlayer
		self.vel = self.vel.normalize().scale(self.spd)
		self.pos -= self.vel

	def update(self, player, range):
		super().update(player,range)

		#line color
		self.currLineColor = (0,0,255)

		#collision and "tag" set up
		if pygame.Rect.colliderect(player.rectangle, self.rectangle):
			if self.It == False:
				self.It = True
			elif self.It == True:
				self.It = False

		#movement
		self.vecToPlayer = player.center - self.center
		if self.vecToPlayer != Vector(0,0):
			self.distance = self.vecToPlayer.length()
		if self.distance < range:
			if self.It == False:
				self.flee()
				self.currLineColor = (0,0,255)
			else:
				self.seek()
				self.currLineColor = (255,0,0)
		

	