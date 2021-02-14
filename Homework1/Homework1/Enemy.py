import pygame

from Agent import Agent
from Vector import Vector
from Constants import Constants

class Enemy(Agent):

	def __init__(self, position, speed, size, color, max_time):
		super().__init__(position, speed, size, color)
		self.clock = pygame.time.Clock()
		self.vecToPlayer = Vector(0,0)
		self.currLineColor = (0,0,255)
		self.idealColor = Constants.ENEMY_COLOR
		self.It = True;
		self.collisionTime = True;
		self.max_time = max_time
		print(max_time)
		self.cur_time = 0.0
		if self.collisionTime: self.cur_time = self.max_time

	def draw(self, screen):
		super().draw(screen)
		
	def lineDraw(self,screen):
		if self.vel != Vector(0,0) :
			self.line_length = self.vel.scale(10)
			pygame.draw.line(screen, self.currLineColor, (self.center.VecX, self.center.VecY), (self.center.VecX + self.line_length.VecX, self.center.VecY + self.line_length.VecY), 4)

	def seek(self):
		self.vel = self.vecToPlayer
		self.vel = self.vel.normalize()
		self.pos += self.vel.scale(self.spd)

	def flee(self):
		self.vel = self.vecToPlayer
		self.vel = self.vel.normalize()
		self.pos -= self.vel.scale(self.spd)

	def colorSwap(self):
		if self.color == self.idealColor:
			self.color = (255,255,255)
			
	#movement
	def movement(self,player):
		self.vecToPlayer = player.center - self.center
		if self.vecToPlayer != Vector(0,0):
			self.distance = self.vecToPlayer.length()
		if self.distance < Constants.ENEMY_RANGE:
			if self.It == False:
				self.flee()
				self.currLineColor = (0,0,255)
			else:
				self.seek()
				self.currLineColor = (255,0,0)

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

		#collision and "tag" set up
		if pygame.Rect.colliderect(player.rectangle, self.rectangle) and self.collisionTime == True:
			print(self.color)
			self.collisionTime = False
			if self.It == False:
				self.It = True
			elif self.It == True:
				self.It = False

		self.movement(player)

		
		

	