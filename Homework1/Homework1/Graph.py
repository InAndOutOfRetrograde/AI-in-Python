import Constants
import Node
import pygame
import Vector

from pygame import *
from Vector import *
from Node import *
from enum import Enum

class SearchType(Enum):
	DJIKSTRA = 1
	A_STAR = 2
	BEST_FIRST = 3

class Graph():
	def __init__(self):
		""" Initialize the Graph """
		self.nodes = []			# Set of nodes
		self.obstacles = []		# Set of obstacles - used for collision detection

		# Initialize the size of the graph based on the world size
		self.gridWidth = int(Constants.WORLD_WIDTH / Constants.GRID_SIZE)
		self.gridHeight = int(Constants.WORLD_HEIGHT / Constants.GRID_SIZE)

		# Create grid of nodes
		for i in range(self.gridHeight):
			row = []
			for j in range(self.gridWidth):
				node = Node(i, j, Vector(Constants.GRID_SIZE * j, Constants.GRID_SIZE * i), Vector(Constants.GRID_SIZE, Constants.GRID_SIZE))
				row.append(node)
			self.nodes.append(row)

		## Connect to Neighbors
		for i in range(self.gridHeight):
			for j in range(self.gridWidth):
				# Add the top row of neighbors
				if i - 1 >= 0:
					# Add the upper left
					if j - 1 >= 0:		
						self.nodes[i][j].neighbors += [self.nodes[i - 1][j - 1]]
					# Add the upper center
					self.nodes[i][j].neighbors += [self.nodes[i - 1][j]]
					# Add the upper right
					if j + 1 < self.gridWidth:
						self.nodes[i][j].neighbors += [self.nodes[i - 1][j + 1]]

				# Add the center row of neighbors
				# Add the left center
				if j - 1 >= 0:
					self.nodes[i][j].neighbors += [self.nodes[i][j - 1]]
				# Add the right center
				if j + 1 < self.gridWidth:
					self.nodes[i][j].neighbors += [self.nodes[i][j + 1]]
				
				# Add the bottom row of neighbors
				if i + 1 < self.gridHeight:
					# Add the lower left
					if j - 1 >= 0:
						self.nodes[i][j].neighbors += [self.nodes[i + 1][j - 1]]
					# Add the lower center
					self.nodes[i][j].neighbors += [self.nodes[i + 1][j]]
					# Add the lower right
					if j + 1 < self.gridWidth:
						self.nodes[i][j].neighbors += [self.nodes[i + 1][j + 1]]

	def getNodeFromPoint(self, point):
		""" Get the node in the graph that corresponds to a point in the world """
		return self.nodes[int(point.y/Constants.GRID_SIZE)][int(point.x/Constants.GRID_SIZE)]

	def placeObstacle(self, point, color):
		""" Place an obstacle on the graph """
		node = self.getNodeFromPoint(point)

		# If the node is not already an obstacle, make it one
		if node.isWalkable:
			# Indicate that this node cannot be traversed
			node.isWalkable = False		

			# Set a specific color for this obstacle
			node.color = color
			for neighbor in node.neighbors:
				neighbor.neighbors.remove(node)
			node.neighbors = []
			self.obstacles += [node]

	def reset(self):
		""" Reset all the nodes for another search """
		for i in range(self.gridHeight):
			for j in range(self.gridWidth):
				self.nodes[i][j].reset()

	def buildPath(self, endNode):
		""" Go backwards through the graph reconstructing the path """
		path = []
		node = endNode
		while node is not 0:
			node.isPath = True
			path = [node] + path
			node = node.backNode

		# If there are nodes in the path, reset the colors of start/end
		if len(path) > 0:
			path[0].isPath = False
			path[0].isStart = True
			path[-1].isPath = False
			path[-1].isEnd = True
		return path

	def findPath_Breadth(self, start, end):
		""" Breadth Search """
		print("BREADTH-FIRST")
		self.reset()

		#Add the start node to the toVisit queue
		startNode = self.getNodeFromPoint(start)
		startNode.isStart = True
		startNode.backNode = 0
		endNode = self.getNodeFromPoint(end)
		endNode.isEnd = True
		toVisit = []
		toVisit.append(startNode)
		startNode.isVisited = True

		while (len(toVisit) > 0):
			#getting the node to edit
			currNode = toVisit.pop(0)
			currNode.isExplored = True

			for nextNode in currNode.neighbors:
				if nextNode.isVisited == False:
					nextNode.isVisited = True
					toVisit.append(nextNode)
					
					nextNode.backNode = currNode

					if nextNode == endNode:
						return self.buildPath(nextNode)

		return []

	def findPath_Djikstra(self, start, end):
		""" Djikstra's Search """
		print("DJIKSTRA")
		self.reset()		

		#Add the start node to the toVisit queue
		startNode = self.getNodeFromPoint(start)
		startNode.isStart = True
		startNode.backNode = 0
		startNode.costFromStart = 0
		startNode.costToEnd = 0
		startNode.cost = 0
		endNode = self.getNodeFromPoint(end)
		endNode.isEnd = True
		toVisit = []
		toVisit.append(startNode)
		startNode.isVisited = True

		while (len(toVisit) > 0):
			#getting the node to edit
			currNode = toVisit.pop(0)
			currNode.isExplored = True
			if currNode == endNode:
				return self.buildPath(currNode)

			for nextNode in currNode.neighbors:
				currDistance = (currNode.center - nextNode.center).length()
				costFromStart = currDistance + currNode.costFromStart
				costToEnd = 0
				cost = costFromStart + costToEnd
				#if you havent visited this node yet
				if nextNode.isVisited == False:
					nextNode.isVisited = True
					#change the costs(cost is the total)
					nextNode.costFromStart = costFromStart
					nextNode.costToEnd = costToEnd
					nextNode.cost = cost

					toVisit.append(nextNode)
					toVisit.sort(key=lambda node:node.cost)
					nextNode.backNode = currNode
				else:
					#check if the new path is cheaper than the old path
					if currDistance + currNode.cost < nextNode.cost:
						#change the cost
						nextNode.costFromStart = costFromStart
						nextNode.costToEnd = costToEnd
						nextNode.cost = cost
						toVisit.sort(key=lambda node:node.cost)
						nextNode.backNode = currNode

		return []

	def findPath_AStar(self, start, end):
		""" A Star Search """
		print("A_STAR")
		self.reset()

		#Add the start node to the toVisit queue
		startNode = self.getNodeFromPoint(start)
		startNode.isStart = True
		startNode.backNode = 0
		startNode.costFromStart = 0
		
		startNode.cost = 0
		endNode = self.getNodeFromPoint(end)
		endNode.isEnd = True

		#guess a distance TO THE END by finding distance between startnode and endnode
		startNode.costToEnd = (endNode.center - startNode.center).length()

		toVisit = []
		toVisit.append(startNode)
		startNode.isVisited = True

		while (len(toVisit) > 0):
			#getting the node to edit
			currNode = toVisit.pop(0)
			currNode.isExplored = True
			if currNode == endNode:
				return self.buildPath(currNode)

			for nextNode in currNode.neighbors:
				currDistance = (currNode.center - nextNode.center).length()
				costFromStart = currDistance + currNode.costFromStart
				costToEnd = (nextNode.center - endNode.center).length()
				cost = costFromStart + costToEnd
				#if you havent visited this node yet
				if nextNode.isVisited == False:
					nextNode.isVisited = True
					#change the costs(cost is the total)
					nextNode.costFromStart = costFromStart
					nextNode.costToEnd = costToEnd
					nextNode.cost = cost

					toVisit.append(nextNode)
					toVisit.sort(key=lambda node:node.cost)
					nextNode.backNode = currNode
				else:
					#check if the new path is cheaper than the old path
					if currDistance + currNode.cost < nextNode.cost:
						#change the cost
						nextNode.costFromStart = costFromStart
						nextNode.costToEnd = costToEnd
						nextNode.cost = cost
						toVisit.sort(key=lambda node:node.cost)
						nextNode.backNode = currNode
		return []

	def findPath_BestFirst(self, start, end):
		""" Best First Search """
		print("BEST_FIRST")
		self.reset()

		#Add the start node to the toVisit queue
		startNode = self.getNodeFromPoint(start)
		startNode.isStart = True
		startNode.backNode = 0
		startNode.costFromStart = 0
		
		startNode.cost = 0
		endNode = self.getNodeFromPoint(end)
		endNode.isEnd = True

		#guess a distance by finding distance between startnode and endnode
		startNode.costToEnd = (startNode.center - endNode.center).length()

		toVisit = []
		toVisit.append(startNode)
		startNode.isVisited = True

		while (len(toVisit) > 0):
			#getting the node to edit
			currNode = toVisit.pop(0)
			currNode.isExplored = True
			if currNode == endNode:
				return self.buildPath(currNode)

			for nextNode in currNode.neighbors:
				currDistance = (currNode.center - nextNode.center).length()
				costFromStart = 0
				costToEnd = (nextNode.center - endNode.center).length()
				cost = costFromStart + costToEnd
				#if you havent visited this node yet
				if nextNode.isVisited == False:
					nextNode.isVisited = True
					#change the costs(cost is the total)
					nextNode.costFromStart = costFromStart
					nextNode.costToEnd = costToEnd
					nextNode.cost = cost

					toVisit.append(nextNode)
					toVisit.sort(key=lambda node:node.cost)
					nextNode.backNode = currNode
				else:
					#check if the new path is cheaper than the old path
					if currDistance + currNode.cost < nextNode.cost:
						#change the cost
						nextNode.costFromStart = costFromStart
						nextNode.costToEnd = costToEnd
						nextNode.cost = cost
						toVisit.sort(key=lambda node:node.cost)
						nextNode.backNode = currNode

		return []

	def draw(self, screen):
		""" Draw the graph """
		for i in range(self.gridHeight):
			for j in range(self.gridWidth):
				self.nodes[i][j].draw(screen)