import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

    def update(self, x):
        self.rect.x = x

    def draw(self, win):
        pygame.draw.rect(win, (0, 255, 0), self.rect)
