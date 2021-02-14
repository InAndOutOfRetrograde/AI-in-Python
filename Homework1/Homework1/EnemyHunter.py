import pygame

from Enemy import Enemy
from Vector import Vector
from Constants import Constants

class EnemyHunter(Enemy):

	def __init__(self, position, speed, size, color, max_time):
		super().__init__(position, speed, size, color, max_time)
		self.timeToPlayer = 0.0
		self.predictedPlayerPos = Vector(0,0)

	#drawing
	def draw(self, screen):
		super().draw(screen)
		pygame.draw.line(screen, (0,0,255), (self.center.VecX, self.center.VecY), (self.futurePosition.VecX, self.futurePosition.VecY), 4)
		
	def lineDraw(self,screen):
		super().lineDraw(screen)

	def colorSwap(self):
		super().colorSwap()

	#behaviors
	def seek(self):
		super().seek()

	def flee(self):
		super().flee()
	
    #Determine the amount of time (t) it would take to get to the Player if we headed straight for where they are right now
    #Assume the Player will continue moving along their current velocity and speed
    #Calculate where the Player will be at time (t) if they continue at their current velocity and speed
    #Head toward that position instead of their current position

	def playerPosPrediction(self, player):
		if(self.vecToPlayer != Vector(0,0)):
			#finding time
			self.timeToPlayer = self.vecToPlayer.length()/Constants.SPEED
			#finding player pos in that time
			#self.predictedPlayerPos = (player.vel.scale(Constants.SPEED * self.timeToPlayer))
			self.futurePosition = player.center + player.vel.scale(self.timeToPlayer)

	#new direction towards based on this vector
	def pursue(self):
		self.vel = self.futurePosition - self.center
		self.vel = self.vel.normalize()
		self.pos += self.vel.scale(self.spd)
	
	#new direction away based on this vector
	def evade(self):
		self.vel = self.futurePosition- self.center
		self.vel = self.vel.normalize()
		self.pos -= self.vel.scale(self.spd)

	def movement(self, player):
		self.vecToPlayer = player.center - self.center
		if self.vecToPlayer != Vector(0,0):
			self.distance = self.vecToPlayer.length()
		if self.distance < Constants.ENEMY_RANGE:
			if self.It == False:
				self.pursue()
				self.currLineColor = (0,0,255)
			else:
				self.evade()
				self.currLineColor = (255,0,0)

	#update lmao
	def update(self, player, range):
		super().update(player, range)
		self.playerPosPrediction(player)
		self.movement(player)
