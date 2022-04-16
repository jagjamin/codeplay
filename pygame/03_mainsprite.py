# -*- coding: utf-8 -*-
from turtle import Screen
import pygame 
pygame.init()

Screen_width = 480
Screen_height = 640
Screen = pygame.display.set_mode((Screen_width, Screen_height))


pygame.display.set_caption("똥피하기-코드플레이")

bg = pygame.image.load("pygame/source/bg.png")

character = pygame.image.load("pygame/source/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_yPos = (Screen_height / 2) - (character_height / 2)
character_xPos = (Screen_width / 2) - (character_width / 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # print("죽여줘")
            running = False
    Screen.blit(bg, (0, 0))
    Screen.blit(character, (character_xPos, character_yPos))
    pygame.display.update()

pygame.quit()
