import pygame

from Agent import Agent
from Vector import Vector
import Constants

class Enemy(Agent):

	def __init__(self, position, speed, size, color, max_time, surface):
		super().__init__(position, speed, size, color, surface)
		self.clock = pygame.time.Clock()
		self.vecToPlayer = Vector(0,0)
		self.currLineColor = (0,0,255)
		self.idealColor = Constants.ENEMY_COLOR
		self.It = True;
		self.collisionTime = True;
		self.max_time = max_time
		self.cur_time = 0.0
		if self.collisionTime: self.cur_time = self.max_time

	def draw(self, screen):
		super().draw(screen)
		
	def lineDraw(self,screen):
		if self.vel != Vector(0,0) :
			self.line_length = self.vel.scale(10)
			pygame.draw.line(screen, self.currLineColor, (self.center.x, self.center.y), (self.center.x - self.line_length.x, self.center.y - self.line_length.y), 4)

	def seek(self):
		self.vel = self.vecToPlayer
		if self.vel.x != 0 or self.vel.y != 0: 
			self.vel = self.vel.normalize().scale(self.maxSpd)
			self.pos += self.vel
		else:
			self.vel = Vector(0,0)

	def flee(self):
		self.vel = self.vecToPlayer
		if self.vel.x != 0 or self.vel.y != 0: 
			self.vel = self.vel.normalize().scale(self.maxSpd)
			self.pos -= self.vel
		else:
			self.vel = Vector(0,0)

	def colorSwap(self):
		if self.color == self.idealColor:
			self.color = (255,255,255)
		
	'''def switchMode(self):
		if self.distance < Constants.ENEMY_RANGE:
			if self.It == False:
				self.flee()
				self.currLineColor = (0,0,255)
			else:
				self.seek()
				self.currLineColor = (255,0,0)
	'''

	#enemy chase movement
	def direction(self,player):
		self.vecToPlayer = player.center - self.center

		if self.vecToPlayer != Vector(0,0):
			self.distance = self.vecToPlayer.length()
		#self.switchMode()

	#collision and "tag" set up
	def collision(self, player):
		if pygame.Rect.colliderect(player.rectangle, self.rectangle) and self.collisionTime == True:
			self.collisionTime = False
			if self.It == False:
				self.It = True
			elif self.It == True:
				self.It = False

	def update(self, player, range):
		super().update(player,range)

		#line color
		self.currLineColor = (0,0,255)

		#timer
		if self.collisionTime == False:
			if self.cur_time <= self.max_time:
				self.colorSwap()
				self.cur_time += 1.0
			elif self.cur_time > self.max_time:
				self.color = self.idealColor
				self.collisionTime = True
				self.cur_time = 0.0

		self.collision(player)
		#self.direction(player)

		
		

	