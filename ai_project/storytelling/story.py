import pygame
import sys

def load_images():
    # 이미지 로드 함수
    image_paths = ['ai_project/storytelling/image/01.png', 'ai_project/storytelling/image/02.png', 
                   'ai_project/storytelling/image/03.png', 'ai_project/storytelling/image/04.png',
                   'ai_project/storytelling/image/05.png', 'ai_project/storytelling/image/06.png',
                   'ai_project/storytelling/image/07.png', 'ai_project/storytelling/image/08.png']
    return [pygame.image.load(path) for path in image_paths]

def draw_text(screen, text, font, color):
    # 텍스트를 화면에 그리는 함수
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width() // 2, screen.get_height() // 2 - 100)  # Y 좌표에 -50을 추가하여 위로 이동
    screen.blit(text_surface, text_rect)

def main():
    # 초기화
    pygame.init()

    # 화면 크기
    screen_size = (1024, 1024)

    # 화면 생성
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("그림 바꾸기")

    # 폰트 설정 (기본 시스템 폰트 사용)
    font_size = 60
    # 폰트 설정 (폰트 파일의 절대 경로를 사용)
    font_path = "ai_project/storytelling/font/D2CodingAll/D2Coding-Ver1.3.2-20180524-all.ttc"
    font = pygame.font.Font(font_path, font_size)

    # 이미지 및 자막 로드
    images = load_images()
    total_images = len(images)
    current_image_index = 0

    image_captions = [
        "첫 번째 이미지 설명",
        "두 번째 이미지 설명",
        "세 번째 이미지 설명",
        "네 번째 이미지 설명",
        "다섯 번째 이미지 설명",
        "여섯 번째 이미지 설명",
        "일곱 번째 이미지 설명",
        "여덟 번째 이미지 설명",
    ]

    current_caption = image_captions[current_image_index]

    # 클릭 횟수 초기화
    click_count = 0

    # 삐용 효과음 로드
    beep_sound = pygame.mixer.Sound("ai_project/storytelling/sounds/Cartoon Jump.mp3")

    # Clock 객체 생성
    clock = pygame.time.Clock()

    # 게임 루프
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 키를 누를 때마다 다음 이미지로 전환 및 삐용 효과음 재생
                if event.key == pygame.K_SPACE:
                    current_image_index = (current_image_index + 1) % total_images
                    current_caption = image_captions[current_image_index]
                    beep_sound.play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 마우스 왼쪽 버튼 클릭
                    # 이미지를 전환하고 삐용 효과음 재생
                    current_image_index = (current_image_index + 1) % total_images
                    current_caption = image_captions[current_image_index]
                    beep_sound.play()
                    # 클릭 횟수 증가
                    click_count += 1

        # 현재 이미지 표시
        screen.blit(images[current_image_index], (0, 0))

        # 이미지에 대한 한글 자막 표시
        draw_text(screen, current_caption, font, (255, 255, 255))

        # 클릭 횟수가 8회인 경우 게임 종료
        if click_count == 8 and current_image_index != total_images - 1:
            pygame.quit()
            sys.exit()

        # 모든 이미지를 보았는지 확인하여 게임 종료
        if current_image_index == total_images - 1:
            if click_count == 8:
                pygame.quit()
                sys.exit()

        # 화면 업데이트
        pygame.display.flip()

        # 초당 프레임 설정
        clock.tick(60)

if __name__ == "__main__":
    main()
