import pygame

pygame.init()

SQUARE_WIDTH = 50
SQUARE_HEIGHT = 50
ROWS = 10
COLUMNS = 12
screen_width = COLUMNS * SQUARE_WIDTH
screen_height = ROWS * SQUARE_HEIGHT

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.position = [0, 0] # Row, Column

        '''
        Row 1. [0, 0, 0, 0, 0]
        Row 2. [0, 0, 0, 0, 0]
        Row 3. [0, 0, 0, 0, 0]
        Row 4. [0, 0, 0, 0, 0]
        Row 5. [0, 0, 0, 0, 0]
        '''

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_DOWN]:
                self.position[0] += 1
            elif keys[pygame.K_UP]:
                self.position[0] -= 1
            elif keys[pygame.K_RIGHT]:
                self.position[1] += 1
            elif keys[pygame.K_LEFT]:
                self.position[1] -= 1

            self.draw()

            pygame.display.flip()

        pygame.quit()

    def draw(self):
        self.screen.fill((255, 255, 255))

        for row in range(ROWS):
            for col in range(COLUMNS):
                x = self.get_x(col)
                y = self.get_y(row)
                pygame.draw.rect(self.screen, (0,0,0), (x, y, SQUARE_WIDTH, SQUARE_HEIGHT))

        # Get the x & y position of the snake
        x = self.get_x(self.position[1])
        y = self.get_y(self.position[0])
        pygame.draw.rect(self.screen, (235,51,36), (x, y, SQUARE_WIDTH, SQUARE_HEIGHT))

    def get_x(self, col):
        return col * SQUARE_WIDTH
    
    def get_y(self, row):
        return row * SQUARE_HEIGHT

if __name__ == "__main__":
    app = App()
    app.run()