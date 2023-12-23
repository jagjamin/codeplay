import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("눈이 내리는 배경과 음악 만들기")

# 배경 이미지 불러오기
original_background = pygame.image.load("ai_project/storytelling/image/zmfl.jpg")
background_image = pygame.transform.scale(original_background, (screen_width, screen_height))
background_rect = background_image.get_rect()

# 배경음악 불러오기
pygame.mixer.music.load("ai_project/storytelling/sounds/zpfhf.mp3")
pygame.mixer.music.play(-1)  # -1은 무한 반복을 의미

# 눈 이미지 불러오기
snowflake_image = pygame.image.load("ai_project/storytelling/image/images-removebg-preview.png")

# 눈송이 리스트
snowflakes = []

# 음악 일시 정지 여부
music_paused = False

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if music_paused:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()
            music_paused = not music_paused

    # 배경 이미지 표시
    screen.blit(background_image, background_rect)

    # 눈이 내리는 모습 표시
    for flake in snowflakes:
        flake[1] += 2  # 눈송이가 아래로 이동하는 속도 조절
        flake[3] += 1  # 눈송이의 회전 각도 조절

        # 크기에 따라 이미지 변환 및 회전
        scaled_snowflake = pygame.transform.scale(snowflake_image, (int(flake[2]), int(flake[2])))
        rotated_snowflake = pygame.transform.rotate(scaled_snowflake, flake[3])
        screen.blit(rotated_snowflake, (flake[0], flake[1]))

    # 눈송이 추가
    if random.random() < 0.02:  # 눈송이를 랜덤하게 추가
        x_position = random.randint(0, screen_width)
        y_position = random.randint(-50, -10)  # 화면 상단(화면 밖)에서 시작
        size = random.uniform(50, 80)  # 최소 크기 설정
        rotation = random.uniform(0, 360)  # 눈송이 회전 각도를 랜덤하게 설정
        snowflakes.append([x_position, y_position, size, rotation])

    # 화면에서 사라진 눈송이 제거
    snowflakes = [flake for flake in snowflakes if flake[1] <= screen_height]

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수 설정
    pygame.time.Clock().tick(60)
