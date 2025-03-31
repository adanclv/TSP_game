import pygame
from src.configs import *

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.start_pos = (x1, y1)
        self.end_pos = (x2, y2)

    def draw(self, screen):
        pygame.draw.line(screen, LINES["color1"], self.start_pos, self.end_pos, LINES["width"])