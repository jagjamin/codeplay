# -*- coding: utf-8 -*-
import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("똥피하기-코드플레이")

bg = pygame.image.load("pygame/source/bg.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # print("죽여줘")
            running = False

    screen.fill((255,255,255))

    pygame.draw.line(screen,(255,0,0), (0,0), (screen_width, screen_height),30)
    pygame.draw.line(screen,(0,255,0), (0,screen_height), (screen_width, 0),30)

    for i in range(0,480,30):
        pygame.draw.line(screen, (0,0,255),(i,0), (i,640))
    for i in range(0,640,30):
        pygame.draw.line(screen, (0,0,255),(0,i), (480,i))

    pygame.draw.circle(screen,(0,255,100), (screen_width / 2, screen_height / 2),100)
    pygame.draw.circle(screen,(0,0,255), (screen_width / 2, screen_height / 2),100,5)

    pygame.draw.rect(screen,(55,55,255), (screen_width / 2, screen_height / 2,100,100))
    pygame.draw.rect(screen,(155,155,55), (screen_width / 2, screen_height / 2,100,100), 5)

    pygame.draw.ellipse(screen,(55,55,255), (screen_width / 2, screen_height / 2,100,100))
    pygame.draw.ellipse(screen,(155,155,55), (screen_width / 2, screen_height / 2,100,100), 5)

    pygame.draw.polygon(screen,(0,0,0), [[100,0], [0,200], [200,200]])
    pygame.draw.polygon(screen,(0,0,0), [[100,0], [0,100], [0,200], [100,300], [200,200], [200,100]])

    pygame.display.update()

pygame.quit()