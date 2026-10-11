import pygame

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 10

    def update(self):
        keys = pygame.key.get.pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed