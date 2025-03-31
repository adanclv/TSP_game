import pygame
from src.configs import *
import math

class Nodo:
    def __init__(self, x, y, image, speed, width, height):
        self.x = x
        self.y = y
        self.angle = 0  # Ángulo inicial
        self.speed = speed
        self.size = (width, height)

        # Cargar imagen
        self.original_image = pygame.image.load(image)
        self.original_image = pygame.transform.scale(self.original_image, self.size)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def rotation(self, screen):
        self.angle += self.speed * 0.01
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        # Mantener la imagen centrada
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    def check_click(self, pos):
        return self.rect.collidepoint(pos)


# TSP en español
# Rectangulos arriba y abajo
# UFO