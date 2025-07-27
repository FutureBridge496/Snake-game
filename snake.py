import pygame

from utils import *

class Snake:
    def __init__(self):
        self.head = [0, 0] # Row, Column

        # 1 -> DOWN
        # 2 -> UP
        # 3 -> RIGHT
        # 4 -> LEFT
        self.direction = 1

        self.body_length = 1
        self.body = [] # (Row, Column), (Row, Column), (Row, Column)
        self.movement_threshold = 30
        self.alive = True

    def draw(self, screen):
        # Get the x & y position of the snake
        x = get_x(self.head[1])
        y = get_y(self.head[0])
        pygame.draw.rect(screen, (235,51,36), (x, y, SQUARE_LENGTH, SQUARE_LENGTH))

        # Draw the body of the snake.
        for i in range(len(self.body)):
            body_x = get_x(self.body[i][1])
            body_y = get_y(self.body[i][0])
            # EVERY square needs to be rendered on the screen
            pygame.draw.rect(screen, (235, 51, 36), (body_x, body_y, SQUARE_LENGTH, SQUARE_LENGTH))

    def move(self):
        if not self.alive:
            return

        self.body.append(list(self.head))

        if len(self.body) > self.body_length:
            items_to_remove = len(self.body) - self.body_length
            self.body = self.body[items_to_remove:]

        if self.direction == 1:
           self.head[0] += 1
        elif self.direction == 2:
           self.head[0] -= 1
        elif self.direction == 3:
           self.head[1] += 1
        elif self.direction == 4:
           self.head[1] -= 1

        self.head[0] = self.head[0] % rows
        self.head[1] = self.head[1] % cols

    def is_eaten(self, apple):
        '''
        Returns true if the snake's head overlaps with the apple.

        Otherwise, it returns false.
        '''
        return self.head == apple.position
    
    def eat(self,apple):
        self.body_length += 1
        self.movement_threshold = max(int(self.movement_threshold * 0.8), 1)
        apple.reposition(self)
        self.move()

    def is_dead(self):
        """The snake is dead when: The head touches the body / the head goes inside the body"""

        return self.head in self.body
