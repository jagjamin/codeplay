import pygame
import sys

# 초기화
pygame.init()

# 화면 크기
screen_size = (1024, 1024)

# 화면 생성
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("그림 바꾸기")

# 이미지 로드
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg', 'image6.jpg', 'image7.jpg', 'image8.jpg']
images = [pygame.image.load(path) for path in image_paths]
current_image_index = 0

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # 키를 누를 때마다 다음 이미지로 전환
            current_image_index = (current_image_index + 1) % len(images)

    # 현재 이미지 표시
    screen.blit(images[current_image_index], (0, 0))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 설정
    pygame.time.Clock().tick(60)
