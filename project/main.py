# -*- coding: utf-8 -*-
import pygame
import random

pygame.init() # 초기화 (반드시 필요)

#화면크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("컨닝오항")


score = 0
gauge = 0

# 새로 들어간 부분 1
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트종류, 크기) none은 기본
total_time = 0
start_ticks = pygame.time.get_ticks() #파이썬상에서 돌아가는 시계의 틱을 받아와 저장.

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    dt = clock.tick(60) #게임화면이 초당 리프레시되는 횟수
    # print("fps : " + str(clock.get_fps())) #화면상의 프레임레이트를 터미널 출력

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

    # 새로들어간 부분 2
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드를 1000으로 나눠 초단위 표시
    timer = game_font.render(str(int(total_time + elapsed_time)), False, (255,255,255)) #소숫점을 짜르기 위해 int로 바꾼 뒤, 문자열로 바꿔 글씨 출력
    screen.fill((0, 0, 0))

    screen.blit(timer, (10, 10))
    pygame.display.update() # 게임화면을 새로고침해줌.

#종료처리
pygame.quit()