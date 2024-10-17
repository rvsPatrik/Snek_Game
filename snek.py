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
ASD = 20
clock = pygame.time.Clock()

item_size = 10
snake_speed = 10
snake_body = [(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)]
snake_direction = None

x,y = 0,0



def generate_food():
    return ( random.randint(0,(SCREEN_WIDTH-item_size) // item_size) * item_size,random.randint(0,(SCREEN_HEIGHT-item_size) // item_size)*item_size)
food_pos = generate_food()


font = pygame.font.SysFont('arialblack',55)

def game_over_msg():
    message = font.render('Game Over Browski',True,GO_TEXT)
    screen.blit(message,[SCREEN_WIDTH//8,SCREEN_HEIGHT//4])
    pygame.display.update()
    time.sleep(2)


running = True

while running:
    snake_direction = pygame.Vector2(0,0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not snake_direction[0]>0:
                x,y = -item_size,0
                snake_direction = pygame.Vector2(-ASD,0)
            if event.key == pygame.K_RIGHT and not snake_direction[0]<0:
                x,y = item_size,0
                snake_direction = pygame.Vector2(ASD,0)
            if event.key == pygame.K_UP and not snake_direction[1]>0:
                x,y = 0,-item_size
                snake_direction = pygame.Vector2(0.-ASD)
            if event.key == pygame.K_DOWN and not snake_direction[1]<0:
                x,y = 0,item_size
                snake_direction = pygame.Vector2(0,ASD)


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

    for i in range (0, (SCREEN_HEIGHT+SCREEN_WIDTH)//2,item_size):
       # pygame.draw.line(screen,SCREEN_COLOR,(i,0),(i))
       pass
    
    for segment in snake_body:
        pygame.draw.rect(screen,SNEK_COLOR,pygame.Rect(segment[0],segment[1],item_size,item_size))
    
    pygame.draw.rect(screen,FOOD_COLOR,pygame.Rect(food_pos[0], food_pos[1],item_size,item_size))


    pygame.display.update()


    clock.tick(snake_speed)





game_over_msg()
pygame.quit()