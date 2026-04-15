import pygame
from settings import *

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        start_pos = [WINDOW_SIZE // 2, WINDOW_SIZE // 2]
        self.body = [start_pos.copy()]
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.grow_next_frame = False

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != DOWN:
            self.next_direction = UP
        elif key == pygame.K_DOWN and self.direction != UP:
            self.next_direction = DOWN
        elif key == pygame.K_LEFT and self.direction != RIGHT:
            self.next_direction = LEFT
        elif key == pygame.K_RIGHT and self.direction != LEFT:
            self.next_direction = RIGHT

    def move(self):
        self.direction = self.next_direction
        head = self.body[0].copy()
        head[0] += self.direction[0] * CELL_SIZE
        head[1] += self.direction[1] * CELL_SIZE
        self.body.insert(0, head)

        if self.grow_next_frame:
            self.grow_next_frame = False
        else:
            self.body.pop()

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, DARK_GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GREEN, (segment[0]+2, segment[1]+2, CELL_SIZE-4, CELL_SIZE-4))

    def check_self_collision(self):
        return self.body[0] in self.body[1:]

    def get_head_pos(self):
        return self.body[0]