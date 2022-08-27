# -*- coding: utf-8 -*-
import pygame
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("컨닝왕")

score = 0
gauge = 0

running = True
while running:
    for event in pygame.event.get()
        if event.type == pygame.QUIT:
            running = False
        if gauge <= 50000:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score += 1
        else:
            gauge = 0
            score = 0
            print("문제풀이 성공")
        if event.typev == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                score = 0
                gauge = 0
    gauge += score
    print(gauge)
pygame.quit