import pygame
import math
import random
import Constants

from Vector import Vector


class Agent:

	def __init__(self, position, speed, size, color, surface):
		self.pos = position
		self.maxSpd = speed
		self.currSpd = 0
		self.vel = Vector(0,0)
		while(self.vel.x == 0):
			self.vel.x = random.uniform(-1.0,1.0)
		while(self.vel.y == 0):
			self.vel.y = random.uniform(-1.0,1.0)
		self.vel.normalize()
		self.surface = surface
		self.siz = size
		self.center = Vector(0,0)
		self.color = color
		self.It = False
		self.rectangle = pygame.Rect(self.pos.x, self.pos.y, self.siz.x, self.siz.y)
		self.rotated_image = surface
	
	def __str__(self):
		return self.center, self.maxSpd, self.pos, self.vel

	def lineDraw(self, screen):
		if self.vel != Vector(0,0):
			self.line_length = self.vel.scale(20)
			pygame.draw.line(screen, (0,0,255), (self.center.x, self.center.y), (self.center.x + self.line_length.x, self.center.y + self.line_length.y), 4)

	#still at an angle for some reason and also straight down shows the line as up
	def rotate(self):
		self.vel.normalize()
		self.angle = math.degrees(math.atan2(-self.currVel.y, self.currVel.x)) - math.degrees(math.pi/2)
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
			self.center = self.pos + Vector((self.siz.x * 0.5), (self.siz.y * 0.5))

		#rect update
		if self.pos.x < 0:
			self.pos.x = 0
		if self.pos.x > Constants.WORLD_WIDTH - self.siz.width:
			self.pos.x = Constants.WORLD_WIDTH - self.siz.width
		if self.pos.y < 0:
			self.pos.y = 0
		if self.pos.y > Constants.WORLD_HEIGHT - self.siz.height:
			self.pos.y = Constants.WORLD_HEIGHT - self.siz.height

		self.rectangle = pygame.Rect(self.pos.x, self.pos.y, self.siz.width, self.siz.height)

		#rotate image
		angle = self.rotate()
		self.rotated_image = pygame.transform.rotate(self.surface, angle)

		
