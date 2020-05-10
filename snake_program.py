import pygame
import time
import random

display_x = 200
display_y = 200
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
snake_width = 10

pygame.init()
window = pygame.display.set_mode((display_x, display_y))
window.fill(white)
pygame.display.set_caption('Welcome to Snake by Bilbobaggins808')
font_style = pygame.font.SysFont(None, 22)


def loss_message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [display_x / 10, display_y / 5])


def score(your_score):
    mesg = font_style.render('Your Score: {0}'.format(str(your_score)), True, blue)
    window.blit(mesg, [0, 0])


def rand_food():
    food_x = round(random.randint(0, display_x - snake_width) / 10.0) * 10.0
    food_y = round(random.randint(0, display_y - snake_width) / 10.0) * 10.0
    return food_x, food_x


def game_loop():
    x1 = display_x / 2
    y1 = display_y / 2
    x_change = 0
    y_change = 0
    (food_x, food_y) = rand_food()
    snake_length = 1
    snake = [(x1, y1)]

    game = True
    session = True

    while session:

        while not game:
            loss_message('You lost! [P]lay again?', blue)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                session = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_width
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = snake_width
                    y_change = 0
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_width
                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_width
        x1 += x_change
        y1 += y_change

        if x1 >= display_x or x1 <= 0 or y1 >= display_y or y1 <= 0:
            game = False

        if [x1, y1] in snake[1:]:
            game = False

        if x1 == food_x and y1 == food_y:
            food_x, food_y = rand_food()
            snake_length += 1

        window.fill(white)
        snake.insert(0, [x1, y1])
        if len(snake) > snake_length:
            snake.pop()

        for cell in snake:
            pygame.draw.rect(window, red, [cell[0], cell[1], snake_width, snake_width])
        pygame.draw.rect(window, blue, [food_x, food_y, snake_width, snake_width])
        score(len(snake) - 1)
        pygame.display.update()

        if snake_length <= 3:
            time.sleep(.1)
        elif snake_length <= 10:
            time.sleep(.09)
        elif snake_length <= 20:
            time.sleep(.08)
        else:
            time.sleep(.07)

    pygame.quit()
    quit()


game_loop()
