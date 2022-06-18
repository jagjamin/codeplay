# -*- coding: utf-8 -*-

import pygame
import random

pygame.init() 


screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("콩 게임-코드플레이")



circleX_pos = 0
circleY_pos = 0

sound_a = pygame.mixer.Sound("pygame/source/Cough2.wav")
sound_b = pygame.mixer.Sound("pygame/source/Doorbell.wav")
sound_c = pygame.mixer.Sound("pygame/source/Squish Pop.wav")

clock = pygame.time.Clock()

character = pygame.image.load("pygame/source/character.png")
#스프라이트의 크기와 좌표 세팅하기 (움직임을 상정한 설정)
character_size = character.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
character_width = character_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
character_height = character_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
character_xPos = (screen_width / 2) - (character_width / 2) #화면 가로 정중앙
character_yPos = screen_height - character_height #화면 세로 맨아래

character_to_x = 0
character_to_y = 0

enemy = pygame.image.load("pygame/source/enemy.png")
#스프라이트의 크기와 좌표 세팅하기 (움직임을 상정한 설정)
enemy_size = enemy.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
enemy_width = enemy_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
enemy_height = enemy_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
enemy_xPos = (screen_width / 2) - (enemy_width / 2) #화면 가로 정중앙
enemy_yPos = (screen_height / 2)- (enemy_height /2)

enemy_to_x = 0
enemy_to_y = 0


ball = pygame.image.load("pygame/source/ball.png")
#스프라이트의 크기와 좌표 세팅하기 (움직임을 상정한 설정)
ball_size = character.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
ball_width = character_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
ball_height = character_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
ball_xPos = (screen_width / 2) - (character_width / 2) #화면 가로 정중앙
ball_yPos = 0 #화면 맨 위

ball_speed_x = 3
ball_speed_y = 3



#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    dt = clock.tick(60)
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False

        if event.type == pygame.KEYDOWN: #키보드 눌림 확인
            if event.key == pygame.K_LEFT: #왼쪽 화살표
                character_to_x -= 1
            elif event.key == pygame.K_RIGHT: #오른쪽 화살표 
                character_to_x += 1

        if event.type == pygame.KEYUP: # 키보드에서 손을 뗐을 때 중지
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #가로움직임
                character_to_x = 0

        mouseX_pos = 0
        mouseY_pos = 0

        if event.type == pygame.MOUSEMOTION:
            mousePos = pygame.mouse.get_pos()
            mouseX_pos = mousePos[0]
            mouseY_pos = mousePos[1]

    character_xPos += character_to_x * dt #스프라이트의 위치 반영
    character_yPos += character_to_y * dt
    # character_yPos += to_y * dt#스프라이트의 위치 반영
    #
    # 가로 스크린내 안벗어나게
    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height

    enemy_xPos = mouseX_pos - (enemy_width / 2)
    enemy_yPos = mouseY_pos - (enemy_height / 2)

    if enemy_xPos < 0:
        enemy_xPos = 0
    elif enemy_xPos > screen_width - enemy_width:
        enemy_xPos = screen_width - enemy_width
    if enemy_yPos < 0:
        enemy_yPos = 0
    elif enemy_yPos > screen_width - enemy_width:
        enemy_yPos = screen_width - enemy_width

    ball_xPos += ball_speed_x
    ball_yPos += ball_speed_y

    if ball_xPos <= 0:
        ball_speed_x *= -1
        ball_speed_x = random.randint(3, 8)

    elif ball_xPos >= screen_width - ball_width:
        ball_speed_x *= -1
        ball_speed_x = -random.randint(3, 8)

    if ball_yPos <= 0:
        ball_speed_y *= -1
        ball_speed_y = random.randint(3, 8)

    elif ball_yPos >= screen_height - ball_height:
        ball_speed_y *= -1
        ball_speed_y = -random.randint(3, 8)




    screen.fill((255, 255, 255))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy, (enemy_xPos, enemy_yPos))
    screen.blit(ball, (ball_xPos, ball_yPos))
    pygame.display.update()

      
    # print("mouseMotion")
    # print(pygame.mouse.get_pos())
    # circleX_pos, circleY_pos = pygame.mouse.get_pos()
    # screen.fill((11,55,26))
    # pygame.draw.circle(screen, (255,0,255), (circleX_pos, circleY_pos), 10)

        
pygame.quit()
            
