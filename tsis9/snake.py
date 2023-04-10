import random

import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 40
pygame.display.set_caption('Snake v0')

def spawn_food(self):
    if not self.food_queue:
        self.food_queue = list(self.food_weights.keys())
        random.shuffle(self.food_queue)
    food_type = self.food_queue.pop(0)
    weight = self.food_weights[food_type]
    x = random.randrange(self.width)
    y = random.randrange(self.height)
    self.food = Food(x, y, weight, food_type)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Food:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    def update(self):
        if self.weight == 1:
            color = YELLOW
        elif self.weight == 2:
            color = GREEN
        else:
            color = PURPLE

        pygame.draw.rect(
            SCREEN,
            color,
            pygame.Rect(
                self.x * BLOCK_SIZE,
                self.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


class Snake:
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
            Point(WIDTH // BLOCK_SIZE // 2 + 1, HEIGHT // BLOCK_SIZE // 2),
        ]
        self.score = 0

    def update(self):
        head = self.points[0]

        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.points[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        self.points[0].x += dx
        self.points[0].y += dy

        head = self.points[0]
        if head.x > WIDTH // BLOCK_SIZE:
            head.x = 0
        elif head.x < 0:
            head.x = WIDTH // BLOCK_SIZE - 1
        elif head.y > HEIGHT // BLOCK_SIZE:
            head.y = 0
        elif head.y < 0:
            head.y = HEIGHT // BLOCK_SIZE - 1

    def check_collision(self, food):
        if self.points[0].x != food.x:
            return 0
        if self.points[0].y != food.y:
            return 0
        return food.weight

    def add_point(self):
        if self.score % 10 == 0:
            self.points.append(Point(self.points[-1].x, self.points[-1].y))


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, (0, y), (WIDTH, y), width=1)


def main():
    running = True
    snake = Snake()
    food_types = [(1, 1), (2, 2), (3, 3)]
    random.shuffle(food_types)
    food_type_idx = 0
    food_weight, food_score = food_types[food_type_idx]
    food = Food(5, 5, food_weight)
    dx, dy = 0, 0
    level = 1
    score = 0

    # create font object
    font = pygame.font.SysFont(None, 30)

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = +1, 0

        snake.move(dx, dy)
        if snake.check_collision(food):
            score += food_score + 2
            while len(snake.points) < score:
                # Add a new point to the end of the snake
                tail = snake.points[-1]
                snake.points.append(Point(tail.x, tail.y))
            while len(snake.points) > score:
                # Remove the last point from the snake
                snake.points.pop()
            if score % 10 == 0:
                level += 1
                clock.tick(5 + level)
            food_type_idx = (food_type_idx + 1) % len(food_types)
            food_weight, food_score = food_types[food_type_idx]
            food = Food(
                random.randint(0, WIDTH // BLOCK_SIZE - 1),
                random.randint(0, HEIGHT // BLOCK_SIZE - 1),
                food_weight
            )

        food.update()
        snake.update()
        draw_grid()

        # create text surface
        text_surface = font.render(f'Level: {level}, Score: {score}', True, WHITE)
        SCREEN.blit(text_surface, (10, 10))

        pygame.display.flip()
        clock.tick(5 + level)


if __name__ == '__main__':
    main()