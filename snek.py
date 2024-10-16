#!/usr/bin/env python3

import pygame
import time

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
ITEM_SIZE = 25

SCREEN_COLOR = "Black"
FOOD_COLOR = "White"
SNEK_COLOR = "Green"

snake_size = 10
snake_speed = 15
snake_body = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]

x,y = 0,0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SNEK')

clock = pygame.time.Clock()

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

    head = (snake_body[0][0])
    snake_body.insert(0,head)
    snake_body.pop()

    screen.fill(SCREEN_COLOR)

    for segment in snake_body:
        pygame.draw.rect(screen,SNEK_COLOR,pygame.Rect(segment[0],segment[1],snake_size,snake_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()