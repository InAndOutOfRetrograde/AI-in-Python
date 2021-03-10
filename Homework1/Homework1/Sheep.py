import pygame

from Enemy import Enemy
from Vector import Vector
from Constants import Constants

class Sheep(Enemy):
    def __init__(self, position, speed, size, color, max_time, surface):
        super().__init__(position, speed, size, color, max_time, surface)
        self.neighbors = []

    def draw(self, screen, herd):
        screen.blit(self.rotated_image, [self.center.VecX - self.siz.width * 0.5, self.center.VecY - self.siz.height * 0.5])
        #pygame.draw.line(screen, (255,0,0), (self.center.VecX, self.center.VecY), (self.center.VecX + (self.cohesVel.VecX * 50), self.center.VecY + (self.cohesVel.VecX * 50)), 3)
        #for sheep in herd:

        pygame.draw.rect(screen, (255,0,0), self.rectangle, 2)
        self.lineDraw(screen)

    def calculateNeighbors(self, herd):
        self.neighbors = []
        for x in range(len(herd)):
            if (herd[x].center - self.center).length() < Constants.SHEEP_RANGE:
                self.neighbors.append(herd[x])
        print(len(self.neighbors))
        return (self.neighbors) 

    def updateAi(self, player, herd):
        #Alignment
        if Constants.enable_align_force:
            self.alignVel = Vector(0,0)
            for x in herd:
                self.alignVel += x.vel
            self.alignVel = self.alignVel.scale(1/len(herd))
            print("alignVel: " + str(self.alignVel))
            self.vel += self.alignVel.normalize().scale(Constants.HERD_ALIGNMENT_FORCE)

        #Cohesion
        if Constants.enable_cohes_force:
            self.cohesVel = Vector(0,0)
            for x in herd:
               self.cohesVel += x.pos
            self.cohesVel = self.cohesVel.scale(1/len(herd))
            self.cohesVel -= self.pos
            self.vel += self.cohesVel.normalize().scale(Constants.HERD_COHESION_FORCE)
            
        #Seperation
        if Constants.enable_seper_force:
            self.sepVel = Vector(0,0)
            for x in herd:
                self.sepVel += (x.pos - self.pos)
            self.sepVel = self.sepVel.scale(1/len(herd))
            self.sepVel = self.sepVel.scale(-1)
            self.vel += self.sepVel.normalize().scale(Constants.HERD_SEPERATION_FORCE)

        #Boundary
        if Constants.enable_bound_force:
            self.boundPos = Vector(0,0)
            boundVel = Vector(0,0)
            if(self.center.VecY < Constants.SHEEP_BOUNDARY_DISTANCE):
                boundVel.VecY += 1
                self.boundPos = Vector(self.center.VecX, 0.0)
            if (self.center.VecY > Constants.WORLD_HEIGHT - Constants.SHEEP_BOUNDARY_DISTANCE):
                boundVel.VecY -= 1
                self.boundPos = Vector(self.center.VecX, Constants.WORLD_HEIGHT)
            if(self.center.VecX < Constants.SHEEP_BOUNDARY_DISTANCE):
                boundVel.VecX += 1
                self.boundPos = Vector(0.0, self.center.VecY)
            if (self.center.VecX > Constants.WORLD_WIDTH - Constants.SHEEP_BOUNDARY_DISTANCE):
                boundVel.VecX -= 1
                self.boundPos = Vector(Constants.WORLD_HEIGHT, self.center.VecY)
            self.vel += boundVel.normalize().scale(Constants.SHEEP_BOUNDARY_FORCE)
            
        #Dog
        if self.distance < Constants.ENEMY_RANGE and Constants.enable_dog_force == True:
            if self.vecToPlayer.VecX != 0 or self.vecToPlayer.VecY != 0: 
                self.vel += self.vecToPlayer.normalize().scale(-Constants.DOG_CHASE_FORCE)

    def update(self, player, range, herd):
        self.currVel = Vector(self.vel.VecX, self.vel.VecY)
        self.direction(player)
        self.updateAi(player, self.calculateNeighbors(herd))
        super().update(player, range)

