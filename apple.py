import random
import pygame

from utils import *

class Apple:
    def __init__(self, snake):
        self.reposition(snake)

    def draw(self, screen):
        apple_x = get_x(self.position[1])
        apple_y = get_y(self.position[0])
        pygame.draw.rect(screen, (150,147,51), (apple_x, apple_y, SQUARE_LENGTH, SQUARE_LENGTH))

    def reposition(self, snake):
        # Modify this function such that the generated position does not overlap the snake's head or body.

        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        self.position = [row,col]

        if (snake.head == self.position) or (self.position in snake.body):
            self.reposition(snake)