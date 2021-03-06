import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)


dis_width = 600
dis_height = 400

WIN = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game.')

clock = pygame.time.Clock()

snake_cords = 10
snake_speed = 15

font_style = pygame.font.SysFont("ubuntu", 25)
score_font = pygame.font.SysFont("ubuntu", 12)


def print_score(score):
    value = score_font.render(f"Your Score:{score} " , True, white)
    WIN.blit(value, [0, 0])


def print_snake(snake_cords, snake_pixels):
    for x in snake_pixels:
        pygame.draw.rect(WIN, green, [x[0], x[1], snake_cords, snake_cords])


def message(msg, color):
    msg = font_style.render(msg, True, color)
    WIN.blit(msg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_pixels = []
    snake_size = 1

    food_x = round(random.randrange(0, dis_width - snake_cords) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_cords) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            WIN.fill(black)
            message("You Lost! Press 1-Play Again or 2-Quit", red)
            print_score(snake_size - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_1:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_cords
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_cords
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_cords
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_cords
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        WIN.fill(black)
        pygame.draw.rect(WIN, green, [food_x, food_y, snake_cords, snake_cords])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_pixels.append(snake_Head)
        if len(snake_pixels) > snake_size:
            del snake_pixels[0]

        for x in snake_pixels[:-1]:
            if x == snake_Head:
                game_close = True

        print_snake(snake_cords, snake_pixels)
        print_score(snake_size - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(
                0, dis_width - snake_cords) / 10.0) * 10.0
            food_y = round(random.randrange(
                0, dis_height - snake_cords) / 10.0) * 10.0
            snake_size += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
