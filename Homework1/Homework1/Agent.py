import pygame
import math
import random

from Vector import Vector
from Constants import Constants

class Agent:

	def __init__(self, position, speed, size, color, surface):
		self.pos = position
		self.maxSpd = speed
		self.currSpd = 0
		self.vel = Vector(0,0)
		while(self.vel.VecX == 0):
			self.vel.VecX = random.uniform(-1.0,1.0)
		while(self.vel.VecY == 0):
			self.vel.VecY = random.uniform(-1.0,1.0)
		self.vel.normalize()
		self.surface = surface
		self.siz = size
		self.center = Vector(0,0)
		self.color = color
		self.It = False
		self.rectangle = pygame.Rect(self.pos.VecX, self.pos.VecY, self.siz.VecX, self.siz.VecY)
		self.rotated_image = surface
	
	def __str__(self):
		return self.center, self.maxSpd, self.pos, self.vel

	def lineDraw(self, screen):
		if self.vel != Vector(0,0):
			self.line_length = self.vel.scale(20)
			pygame.draw.line(screen, (0,0,255), (self.center.VecX, self.center.VecY), (self.center.VecX + self.line_length.VecX, self.center.VecY + self.line_length.VecY), 4)

	#still at an angle for some reason and also straight down shows the line as up
	def rotate(self):
		self.vel.normalize()
		self.angle = math.degrees(math.atan2(-self.currVel.VecY, self.currVel.VecX)) - math.degrees(math.pi/2)
		return self.angle

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rectangle)
		self.lineDraw(screen)

	def update(self, player, range):

		#slowed turn vel
		#self.currVel.lerp(Constants.SHEEP_TURN_SPEED, self.vel)
		#move
		self.pos += self.vel.normalize().scale(self.maxSpd)

		#center update
		if(self.surface != None):
			self.siz = self.rotated_image.get_bounding_rect()
			self.center = self.pos + Vector((self.siz.width * 0.5), (self.siz.height * 0.5))
		else:
			self.center = self.pos + Vector((self.siz.VecX * 0.5), (self.siz.VecY * 0.5))

		#rect update
		if self.pos.VecX < 0:
			self.pos.VecX = 0
		if self.pos.VecX > Constants.WORLD_WIDTH - self.siz.width:
			self.pos.VecX = Constants.WORLD_WIDTH - self.siz.width
		if self.pos.VecY < 0:
			self.pos.VecY = 0
		if self.pos.VecY > Constants.WORLD_HEIGHT - self.siz.height:
			self.pos.VecY = Constants.WORLD_HEIGHT - self.siz.height

		self.rectangle = pygame.Rect(self.pos.VecX, self.pos.VecY, self.siz.width, self.siz.height)

		#rotate image
		angle = self.rotate()
		self.rotated_image = pygame.transform.rotate(self.surface, angle)

		
