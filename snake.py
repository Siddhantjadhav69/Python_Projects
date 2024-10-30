import pygame
import sys
import random
import time

# Direction Constants
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

class SnakeGame:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.direction = RIGHT
        self.snake_list = [(200, 200), (220, 200), (240, 200)]
        self.food = self.new_food()

    def new_food(self):
        while True:
            food = (random.randint(0, self.width - 20) // 20 * 20, 
                    random.randint(0, self.height - 20) // 20 * 20)
            if food not in self.snake_list:
                return food

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction!= DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN and self.direction!= UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction!= RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction!= LEFT:
                        self.direction = RIGHT

            head = self.snake_list[-1]
            if self.direction == UP:
                new_head = (head[0], head[1] - 20)
            elif self.direction == DOWN:
                new_head = (head[0], head[1] + 20)
            elif self.direction == LEFT:
                new_head = (head[0] - 20, head[1])
            elif self.direction == RIGHT:
                new_head = (head[0] + 20, head[1])

            self.snake_list.append(new_head)

            if self.food == new_head:
                self.food = self.new_food()
            else:
                self.snake_list.pop(0)

            # Game Over Conditions
            if (new_head[0] < 0 or new_head[0] >= self.width or 
                new_head[1] < 0 or new_head[1] >= self.height or 
                new_head in self.snake_list[:-1]):
                print("Game Over!")
                time.sleep(1)
                self.reset_game()

            # Draw Everything
            self.display.fill((0, 0, 0))
            for pos in self.snake_list:
                pygame.draw.rect(self.display, (0, 255, 0), (pos[0], pos[1], 20, 20))
            pygame.draw.rect(self.display, (255, 0, 0), (self.food[0], self.food[1], 20, 20))
            pygame.display.update()

            self.clock.tick(10)  # Speed of the game

if __name__ == "__main__":
    game = SnakeGame()
    game.play()