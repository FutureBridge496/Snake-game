import pygame

from snake import Snake
from utils import *
from apple import Apple

pygame.init()

# Hint: Use a variable for the direction. It could be an integer with 4 possible values: 1, 2, 3, 4 where 1 is UP, 2 is DOWN, etc. 
#       Then, when the user presses a key, change the direction variable's value.
#       In the game loop, change the position of the snake based on the direction i.e move the snake based on the direction variable instead of key presses like you're doing right now.

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        self.snake = Snake()

        self.apple = Apple(self.snake)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        frame_counter = 0

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

            if (frame_counter % self.snake.movement_threshold) == 0:
                self.snake.move()

                if self.snake.is_eaten(self.apple):
                    self.snake.eat(self.apple)

                if self.snake.is_dead():
                    self.snake.alive = False
                    
            if not self.snake.alive:
                self.draw_game_over_screen()
            else:
                self.draw()

            pygame.display.flip()
            

        pygame.quit()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.apple.draw(self.screen)
    
        # Add the previous head position to the body.

        # Make sure the body is the current length.

        # Body Length: 2
        # [x, x, x, x, x]
        # I have to remove the first "3"

    def draw_game_over_screen(self):
        self.screen.fill((255, 255, 255))

        title_font = pygame.font.SysFont(None, 96)
        title_render = title_font.render("GAME OVER", False, (0, 0, 0))

        title_x = (SCREEN_WIDTH / 2) - (title_render.get_width() / 2)
        title_y = 200
        self.screen.blit(title_render, (title_x, title_y))

        score = f"Score: {self.snake.body_length - 1} "

        score_font = pygame.font.SysFont(None, 30)
        score_render = score_font.render(score, False, (237, 28, 36))

        score_x = (SCREEN_WIDTH / 2) - (score_render.get_width() / 2)
        score_y = 300
        self.screen.blit(score_render, (score_x, score_y))

if __name__ == "__main__":
    app = App()
    app.run()