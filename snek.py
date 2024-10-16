#!/usr/bin/env python3

import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SNEK')

SCREEN_COLOR = (0,0,0)
FOOD_COLOR = (255,255,255)
SNEK_COLOR = (0,255,0)
GO_TEXT = (255,0,0)

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 10
snake_body = [(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)]

x,y = 0,0



def generate_food():
    return ( random.randint(0,(SCREEN_WIDTH-snake_size) // snake_size) * snake_size,random.randint(0,(SCREEN_HEIGHT-snake_size) // snake_size)*snake_size)
food_pos = generate_food()


font = pygame.font.SysFont('arialblack',55)

def game_over_msg():
    message = font.render('Game Over Browski',True,GO_TEXT)
    screen.blit(message,[SCREEN_WIDTH//8,SCREEN_HEIGHT//4])
    pygame.display.update()
    time.sleep(2)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x,y = -snake_size,0
            elif event.key == pygame.K_RIGHT:
                x,y = snake_size,0
            elif event.key == pygame.K_UP:
                x,y = 0,-snake_size
            elif event.key == pygame.K_DOWN:
                x,y = 0,snake_size


    head = (snake_body[0][0] + x, snake_body[0][1] + y)
    snake_body.insert(0,head)
    snake_body.pop()

    if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
        running = False

    if snake_body[0] == food_pos:
        food_pos = generate_food()
        snake_body.append(snake_body[-1])
        snake_speed+=2

    screen.fill(SCREEN_COLOR)


    
    for segment in snake_body:
        pygame.draw.rect(screen,SNEK_COLOR,pygame.Rect(segment[0],segment[1],snake_size,snake_size))
    
    pygame.draw.rect(screen,FOOD_COLOR,pygame.Rect(food_pos[0], food_pos[1],snake_size,snake_size))


    pygame.display.update()


    clock.tick(snake_speed)





game_over_msg()
pygame.quit()