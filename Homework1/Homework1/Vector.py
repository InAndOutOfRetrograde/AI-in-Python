import math

class Vector:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		 return "Vector" + str(self.x) + ", " + str(self.y)

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __sub__ (self, other):
		return Vector(self.x - other.x, self.y - other.y)
	
	def dot(self, other):
		return Vector((self.x, self.y) @ (other.x,other.y))

	def scale(self, scalar):
		return Vector(self.x*scalar, self.y*scalar)
	
	def length(self):
		return math.sqrt((self.x ** 2) + (self.y ** 2))

	def normalize(self):
		mag = self.length()
		if(mag > 0):
			self.x = self.x/mag
			self.y = self.y/mag
		return self

	def lerp(self, strength, target):
		self = self + target.scale(strength)
		return self 