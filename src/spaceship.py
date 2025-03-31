import pygame
from src.configs import *
import math

class Spaceship:
    def __init__(self, x, y):
        self.shape = pygame.Rect(0, 0, SHAPE_SPACESHIP['width'], SHAPE_SPACESHIP['height'])
        self.shape.center = (x, y)
        self.target_x = x
        self.target_y = y
        self.image = pygame.image.load(SHAPE_SPACESHIP['path_imgufo'])
        self.angle = 0
        self.rotation = 0  # Ángulo de rotación inicial

        self.frames = [
            self.get_image(self.image, 0, 240, 196),
            self.get_image(self.image, 1, 240, 196),
            self.get_image(self.image, 2, 240, 196),
            self.get_image(self.image, 3, 240, 196), # 16 x 24
            self.get_image(self.image, 4, 240, 196),
            self.get_image(self.image, 5, 240, 196),
            self.get_image(self.image, 6, 240, 196),
            self.get_image(self.image, 7, 240, 196),
        ]
        self.frame_index = 0

    def draw(self, screen, imagen):
        screen.blit(imagen, (self.shape.centerx, self.shape.centery))
        #pygame.draw.rect(screen, (255, 0, 0), self.shape, 2)  # Color rojo con un grosor de 2

    def get_image(self, sheet, frame, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (int(width * 0.25), int(height * 0.25)))
        image.set_colorkey((0, 0, 0))
        return image

    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y

    def distancia_target(self):
        return math.sqrt((self.target_x - self.shape.x) ** 2 + (self.target_y - self.shape.y) ** 2)

    def rotate(self, angle):
        pass

    def move_towards(self):
        """Mueve la nave gradualmente hacia el objetivo."""
        dx = self.target_x - self.shape.x
        dy = self.target_y - self.shape.y
        distance = math.sqrt(dx ** 2 + dy ** 2)  # Distancia a la meta

        # Si la nave está suficientemente cerca del objetivo
        if distance > 1:  # Solo moverse si no ha llegado
            # Normalizar la dirección y mover en pequeños pasos
            direction_x = dx / distance
            direction_y = dy / distance

            self.shape.x += direction_x * SHAPE_SPACESHIP['speed']
            self.shape.y += direction_y * SHAPE_SPACESHIP['speed']

            # Calcular el ángulo hacia el destino (hacia el nodo)
            angle = math.atan2(dy, dx)  # Calcular el ángulo hacia el objetivo
            self.rotate(angle)  # Rotar la nave hacia el ángulo calculado
