import pygame

from Player import Player
from Vector import Vector
import Constants

class Dog(Player):
    def __init__(self, position, speed, size, color, surface):
        super().__init__(position, speed, size, color, surface)

    def draw(self, screen):
        screen.blit(self.rotated_image, [self.center.x - self.siz.width * 0.5, self.center.y - self.siz.height * 0.5])
        pygame.draw.rect(screen, (255,0,0), self.rectangle, 2)
        self.lineDraw(screen)

    def update(self, player, range):
        self.currVel = Vector(self.vel.x, self.vel.y)
        super().update(player, range)