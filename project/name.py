# -*- coding: utf-8 -*-
import pygame
import random

pygame.init()

#화면크기 설정
screen_width = 640 # 가로크기
screen_height = 480 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("앱이름")

#이미지들

bg = pygame.image.load("project_2p2j/source/bg.png")
bg2 = pygame.image.load("project_2p2j/source/bg2.png")
# bg2_size = character.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
bg2_width = 90 #위에서 얻은 튜플의 1번째 값. 자동생성
bg2_height = 480#위에서 얻은 튜플의 2번째 값. 자동생성.
bg2_xPos = screen_width - bg2_width #화면 가로 정중앙
bg2_yPos = 0 #화면 세로 맨아래


character = pygame.image.load("project_2p2j/source/character.png")
character_size = character.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
character_width = character_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
character_height = character_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
character_xPos = screen_width / 2 - character_width / 2 #화면 가로 정중앙
character_yPos = screen_height - character_height * 2 #화면 세로 맨아래



enemy = pygame.image.load("project_2p2j/source/enemy.png")
enemy_size = enemy.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
enemy_width = enemy_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
enemy_height = enemy_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
enemy_xPos = (screen_width / 2) - (enemy_width / 2)#화면 가로 정중앙
enemy_yPos = 50



#FPS
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

#글씨쓰기
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트종류, 크기) none은 기본

gauge = 0
score = 0

running = True #실행중인지 확인
while running:
    dt = clock.tick(60) #게임화면이 초당 리프레시되는 횟수
    ten_sec = (int((pygame.time.get_ticks() - start_ticks) / 1000)) % 10
    # print(ten_sec)
    time_screen = game_font.render(str(ten_sec + 1), False, (100, 0, 0))

    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT:
            running = False
        if gauge <= 100:
            if event.type == pygame.KEYDOWN: #키보드 눌림 확인
                if event.key == pygame.K_SPACE: #왼쪽 화살표
                    score += 1
        else:
            gauge = 0
            score = 0
            print("문제풀이 성공")
        if event.type == pygame.KEYUP: # 키보드에서 손을 뗐을 때 중지
            if event.key == pygame.K_SPACE:
                score = 0
                gauge = 0
    gauge += score
    print(gauge)
    
        
    #3. 게임 캐릭터 위치 정의

    #4. 충돌처리

    #5. 화면에 그리기
    screen.fill((255, 255, 255))
    # screen.blit
    screen.blit(bg2, (bg2_xPos, bg2_yPos)) # blit = 배경 그리기
    screen.blit(character, (character_xPos, character_yPos)) #주인공 그리기
    screen.blit(enemy, (enemy_xPos, enemy_yPos))
    screen.blit(time_screen, (10, 10))
    pygame.draw.rect(screen, (55, 55, 255), (character_xPos, character_yPos - 10, gauge, 10))

    pygame.display.update() # 게임화면을 새로고침해줌.

#종료시간 살짝 늦추기
# pygame.time.delay(2000)

#종료처리
pygame.quit()