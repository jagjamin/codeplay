# -*- coding: utf-8 -*-
from turtle import Screen
import pygame 
pygame.init()

Screen_width = 480
Screen_height = 640
Screen = pygame.display.set_mode((Screen_width, Screen_height))


pygame.display.set_caption("똥피하기-코드플레이")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # print("죽여줘")
            running = False


pygame.quit()
