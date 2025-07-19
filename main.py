import pygame

from snake import Snake

pygame.init()

SQUARE_LENGTH = 30
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 60

rows = int(SCREEN_HEIGHT / SQUARE_LENGTH)
cols = int(SCREEN_WIDTH / SQUARE_LENGTH)

# Hint: Use a variable for the direction. It could be an integer with 4 possible values: 1, 2, 3, 4 where 1 is UP, 2 is DOWN, etc. 
#       Then, when the user presses a key, change the direction variable's value.
#       In the game loop, change the position of the snake based on the direction i.e move the snake based on the direction variable instead of key presses like you're doing right now.

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        self.snake = Snake()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        frame_counter = 0
        movement_threshold = 30

        while running:
            clock.tick(FPS)
            frame_counter += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_DOWN]:
                self.snake.direction = 1
            elif keys[pygame.K_UP]:
                self.snake.direction = 2
            elif keys[pygame.K_RIGHT]:
                self.snake.direction = 3
            elif keys[pygame.K_LEFT]:
                self.snake.direction = 4

            if (frame_counter % movement_threshold) == 0:    
                self.move()

            self.draw()

            pygame.display.flip()
            

        pygame.quit()

    def draw(self):
        self.screen.fill((255, 255, 255))

        for row in range(rows):
            for col in range(cols):
                x = self.get_x(col)
                y = self.get_y(row)
                pygame.draw.rect(self.screen, (0,0,0), (x, y, SQUARE_LENGTH, SQUARE_LENGTH))

        # Get the x & y position of the snake
        x = self.get_x(self.snake.position[1])
        y = self.get_y(self.snake.position[0])
        pygame.draw.rect(self.screen, (235,51,36), (x, y, SQUARE_LENGTH, SQUARE_LENGTH))
        
    def get_x(self, col):
        return col * SQUARE_LENGTH
    
    def get_y(self, row):
        return row * SQUARE_LENGTH
    
    def move(self):
         if self.snake.direction == 1:
            self.snake.position[0] += 1
         elif self.snake.direction == 2:
            self.snake.position[0] -= 1
         elif self.snake.direction == 3:
            self.snake.position[1] += 1
         elif self.snake.direction == 4:
            self.snake.position[1] -= 1

if __name__ == "__main__":
    app = App()
    app.run()