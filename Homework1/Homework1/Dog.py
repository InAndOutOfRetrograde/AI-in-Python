import pygame

from Player import Player
from Vector import Vector
from Constants import Constants

class Dog(Player):
    def __init__(self, position, speed, size, color, surface):
        super().__init__(position, speed, size, color, surface)

    def draw(self, screen):
        screen.blit(self.rotated_image, [self.center.VecX - self.siz.width * 0.5, self.center.VecY - self.siz.height * 0.5])
        pygame.draw.rect(screen, (255,0,0), self.rectangle, 2)
        self.lineDraw(screen)

    def update(self, player, range):
        self.currVel = Vector(self.vel.VecX, self.vel.VecY)
        super().update(player, range)