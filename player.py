import pygame

class Player():
    def __init__(self, spawnX, spawnY) -> None:
        self.x = spawnX
        self.y = spawnY
        self.color = (10, 10, 10)
        self.radius = 30
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)