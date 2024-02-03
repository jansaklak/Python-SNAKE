import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 240, 160
GRID_SIZE = 10
SNAKE_SIZE = 10
FPS = 8

WHITE =     (255, 255, 255)
RED =       (255, 0, 0)
GREEN =     (0, 255, 0)
BLUE =      (0,0,255)
BLACK =     (5,5,5)
BACKGROUND= (170,220,2)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.grid_size = GRID_SIZE
        self.snake_size = SNAKE_SIZE
        self.fps = FPS

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake')

        self.clock = pygame.time.Clock()

        self.snake = [(0, self.height // 2)]
        self.direction = RIGHT
        self.foods = self.foods_position()

    def foods_position(self):
        while True:
            food =   (random.randint(0, self.width  // self.grid_size - 1) * self.grid_size,
                      random.randint(0, self.height // self.grid_size - 1) * self.grid_size)
            poison = (random.randint(0, self.width  // self.grid_size - 1) * self.grid_size,
                      random.randint(0, self.height // self.grid_size - 1) * self.grid_size)
            if food not in self.snake and food not in poison:
                foods = [food,poison]
                return foods

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, BLACK, (segment[0], segment[1], self.snake_size, self.snake_size))

    def draw_foods(self):
            pygame.draw.rect(self.screen, BLUE, (self.foods[0][0], self.foods[0][1], self.snake_size, self.snake_size))
            pygame.draw.rect(self.screen, RED,  (self.foods[1][0], self.foods[1][1], self.snake_size, self.snake_size))

    def snake_move(self):
        head = list(self.snake[0])
        head[0] += self.direction[0] * self.grid_size
        head[1] += self.direction[1] * self.grid_size
        
        if (
            head[0] < 0     or   head[0] >= self.width      or     head[1] < 0       or      head[1] >= self.height      or      tuple(head) in self.snake[1:]
        ):  self.game_over()

        self.snake.insert(0, tuple(head))

        if tuple(head) == (self.foods[0][0],self.foods[0][1]):
            self.foods = self.foods_position()
        elif tuple(head) == (self.foods[1][0],self.foods[1][1]):
            self.snake.pop()
            if(len(self.snake)==1): self.game_over()
            self.snake.pop()
            self.foods = self.foods_position()
        else:
            self.snake.pop()

    def game_over(self):
        print("Koniec gry")
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP      and self.direction != DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN  and self.direction != UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT  and self.direction != RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT
            self.snake_move()
            self.screen.fill(BACKGROUND)
            self.draw_snake()
            self.draw_foods()

            pygame.display.flip()
            self.clock.tick(self.fps)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
