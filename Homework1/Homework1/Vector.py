import math

class Vector:

	def __init__(self, x, y):
		self.VecX = x
		self.VecY = y

	def __str__(self):
		 print ("Vector", Vector.VecX, ", ", Vector.VecY)

	def __add__(self, other):
		return Vector(self.VecX + other.VecX, self.VecY + other.VecY)

	def __sub__ (self, other):
		return Vector(self.VecX - other.VecX, self.VecY - other.VecY)
	
	def dot(self, other):
		return Vector((self.VecX, self.VecY) @ (other.VecX,other.VecY))

	def scale(self, scalar):
		return Vector(self.VecX*scalar, self.VecY*scalar)
	
	def length(self):
		return math.sqrt((self.VecX ** 2) + (self.VecY ** 2))

	def normalize(self):
		mag = self.length()
		if(mag > 0):
			self.VecX = self.VecX/mag
			self.VecY = self.VecY/mag
		return self