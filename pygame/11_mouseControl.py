# -*- coding: utf-8 -*-

import pygame

pygame.init() 


screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기-코드플레이")

circleX_pos = 0
circleY_pos = 0

sound_a = pygame.mixer.Sound("pygame/source/Cough2.wav")
sound_b = pygame.mixer.Sound("pygame/source/Doorbell.wav")
sound_c = pygame.mixer.Sound("pygame/source/Squish Pop.wav")

clock = pygame.time.Clock()



#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    dt = clock.tick(60)
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False

        if event.type == pygame.MOUSEMOTION:
            print("mouseMotion")
            print(pygame.mouse.get_pos())
            circleX_pos, circleY_pos = pygame.mouse.get_pos()
            screen.fill((11,55,26))
            pygame.draw.circle(screen, (255,0,255), (circleX_pos, circleY_pos), 10)

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("버튼을 누르셨습니다")
            print(pygame.mouse.get_pos())
            print(event.button)
            if event.button == 1:
                print("좌클")
                sound_a.play()
            elif event.button == 3:
                print("우클")
                sound_b.play()
            elif event.button == 2:
                print("휠클")
                sound_c.play()
            elif event.button == 4:
                print("휠업")
            elif event.button == 5:
                print("휠다운")
        
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouseBottonup")
            pass

    pygame.display.update()

pygame.quit()
            
