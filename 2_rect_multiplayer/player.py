import pygame

class Player:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = 5
        
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        self.update()

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
    