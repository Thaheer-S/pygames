import pygame
import random

pygame.init()

width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
c = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("calibri", 50)
score_font = pygame.font.SysFont("calibri", 20)

paused = False


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, (0, 0, 0))
    screen.blit(value, [0, 0])


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 0, 255), [x[0], x[1], snake_block, snake_block])  # Change snake color to blue


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    global paused
    running = True
    while running:

        while game_close:
            screen.fill((0, 0, 0))
            message("You Lost! Press R to Restart or Q to Quit", (255, 0, 0))
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_close = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gameLoop()  # Restart the game
                    elif event.key == pygame.K_q:
                        running = False
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change -= snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change += snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change -= snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change += snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:
                    paused = not paused  # Toggle pause state

        if not paused:
            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            screen.fill((211, 211, 211))  # Set the background color to light gray

            pygame.draw.rect(screen, (255, 0, 0), [foodx, foody, snake_block, snake_block])  # Change food color to red

            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

        c.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
