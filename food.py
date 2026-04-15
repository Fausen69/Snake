import random
import pygame
from settings import *

class Food:
    def __init__(self):
        self.position = [0, 0]

    def spawn(self, snake_body):
        while True:
            pos = [random.randint(0, GRID_SIZE - 1) * CELL_SIZE,
                   random.randint(0, GRID_SIZE - 1) * CELL_SIZE]
            if pos not in snake_body:
                self.position = pos
                return

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

    def is_eaten(self, snake_head):
        return snake_head == self.position