# -*- coding: utf-8 -*-
import pygame

############################################################################
#파이게임 초기설정 (반드시 초기에 세 해야하는 것)
pygame.init()

#화면크기
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("앱이름")

#FPS
clock = pygame.time.Clock()
##############################################

#1. 사용자가 추가하는 내용들 초기화 (배경, 스프라이트, 좌표, 속도, 폰트, 변수,시간 등)

#이벤트 반복 시작 - 스크래치의 무한반복과 같음
running = True #실행중인지 확인
while running:
    dt = clock.tick(60)

    #2. 이벤트 처리(키보드 마우스 등 화면조작 관련)
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False

    #3. 게임 캐릭터 위치 정의 

    #4. 충돌처리

    #5.화면에 그리기
    pygame.display.update() # 게임화면을 새로고침해줌.

pygame.time.delay(2000)

#종료처리
pygame.quit()
