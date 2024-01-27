import pygame
import sys
import random
import time


# 초기화
pygame.init()
pygame.mixer.init()  # 사운드를 위한 초기화

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Galaga Clone")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# 폰트 설정 (직접 폰트 파일 경로 지정)
font_path = "ai_project/storytelling/font/k_font.ttf"  # 여기에 폰트 파일 경로를 입력하세요
font = pygame.font.Font(font_path, 36)


# 플레이어 설정
player_width, player_height = 30, 30
player_x = (width - player_width) // 2
player_y = height - player_height - 20
player_speed = 5
player_image_path = "ai_project\storytelling\image\994499345CC6CE7E03-removebg-preview.png"  # 이미지 파일 경로
player_image = pygame.image.load(player_image_path)
player_image = pygame.transform.scale(player_image, (player_width, player_height))

# 총알 설정
bullet_width, bullet_height = 5, 15
bullet_speed = 4
bullets = []
shoot_delay = 0

# 적 설정
enemy_width, enemy_height = 30, 30
enemy_speed = 1
enemies = []
enemy_image_path = "ai_project\storytelling\image\스크린샷_2024-01-27_121632-removebg-preview.png"  # 이미지 파일 경로
enemy_image = pygame.image.load(enemy_image_path)
enemy_image = pygame.transform.scale(enemy_image, (enemy_width, enemy_height))


# 목숨 설정
lives = 3
life_image = pygame.image.load("ai_project\storytelling\image\pngtree-beautiful-bright-red-heart-png-image_6252575-removebg-preview.png")  # 목숨 이미지 불러오기
life_image = pygame.transform.scale(life_image, (20, 20))  # 이미지 크기 조절

# 점수 초기화
score = 0

# 사운드 로드
shoot_sound = pygame.mixer.Sound("ai_project\storytelling\sounds\Pew.wav")  # 총알 발사 사운드
explosion_sound = pygame.mixer.Sound("ai_project\storytelling\sounds\Bonk.wav")  # 폭발 사운드

# 게임 상태
is_game_over = False


def reset_game():
    global player_x, player_y, bullets, enemies, score, lives, is_game_over
    player_x = (width - player_width) // 2
    player_y = height - player_height - 20
    bullets = []
    enemies = []
    score = 0
    lives = 3
    is_game_over = False
    for _ in range(initial_enemies_count):
        spawn_enemy()

# 적 생성 함수
def spawn_enemy():
    enemy_x = random.randint(0, width - enemy_width)
    enemy_y = random.randint(-100, -enemy_height)
    enemies.append({'x': enemy_x, 'y': enemy_y, 'alive': True})

# 적과 총알 충돌 여부 확인 함수
def is_collision(obj1, obj2):
    return (
        obj1['x'] < obj2['x'] + enemy_width and
        obj1['x'] + enemy_width > obj2['x'] and
        obj1['y'] < obj2['y'] + enemy_height and
        obj1['y'] + enemy_height > obj2['y']
    )

# 점수 증가 함수
def increase_score():
    global score
    score += 1

# 총알과 적 충돌 처리 함수
def handle_enemy_hit(bullet, enemy):
    if is_collision(bullet, enemy) and enemy['alive']:
        bullets.remove(bullet)
        enemy['alive'] = False
        spawn_enemy()
        increase_score()

# 플레이어와 적 충돌 처리 함수
def handle_player_enemy_collision():
    global lives, is_game_over
    for enemy in enemies[:]:
        if is_collision({'x': player_x, 'y': player_y}, enemy) and enemy['alive']:
            explosion_sound.play()  # 폭발 사운드 재생
            enemies.remove(enemy)
            spawn_enemy()
            lives -= 1
            if lives <= 0:
                is_game_over = True
            return  # 목숨을 한 번만 잃게 하기 위해 루프 탈출

# 목숨 표시 함수
def display_lives():
    for i in range(lives):
        life_rect = life_image.get_rect()
        life_rect.topleft = (width - (i + 1) * life_rect.width, 10)
        screen.blit(life_image, life_rect)

# 게임 오버 화면 표시 함수
def display_game_over():
    game_over_text = font.render("게임 오버", True, red)
    game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2))
    screen.blit(game_over_text, game_over_rect)

# 게임 초기화 부분에 적 생성
initial_enemies_count = 5
for _ in range(initial_enemies_count):
    spawn_enemy()


# 총알 발사 간격 설정
shoot_delay_max = 15
shoot_delay_increment = 10

# 점수 증가 함수 수정
def increase_score():
    global score, shoot_delay_max
    score += 1
    if score % 100 == 0:  # 점수가 100의 배수일 때
        shoot_delay_max += shoot_delay_increment



# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    if is_game_over:
        display_game_over()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            reset_game()
        pygame.display.flip()
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    if keys[pygame.K_SPACE] and shoot_delay == 0:
        shoot_sound.play()  # 총알 발사 사운드 재생
        bullet_x = player_x + (player_width - bullet_width) // 2
        bullet_y = player_y
        bullets.append({'x': bullet_x, 'y': bullet_y})
        shoot_delay = shoot_delay_max  # 발사 간격 적용

    if shoot_delay > 0:
        shoot_delay -= 1

    for bullet in bullets:
        bullet['y'] -= bullet_speed
        if bullet['y'] < 0:
            bullets.remove(bullet)

    # 적과 총알 충돌 처리
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            handle_enemy_hit(bullet, enemy)

    # 플레이어와 적 충돌 처리
    handle_player_enemy_collision()

    screen.fill(white)
    pygame.draw.rect(screen, blue, [player_x, player_y, player_width, player_height])

    for enemy in enemies:
        if enemy['alive']:
            pygame.draw.rect(screen, red, [enemy['x'], enemy['y'], enemy_width, enemy_height])
            enemy['y'] += enemy_speed
            if enemy['y'] > height:
                enemy['alive'] = False
                spawn_enemy()

    for bullet in bullets:
        pygame.draw.rect(screen, green, [bullet['x'], bullet['y'], bullet_width, bullet_height])

    display_lives()

    score_text = font.render("점수: {}".format(score), True, black)
    screen.blit(score_text, (10, 10))

    # 플레이어 그리기 대신 이미지 표시
    screen.blit(player_image, (player_x, player_y))
    
    for enemy in enemies:
        if enemy['alive']:
            screen.blit(enemy_image, (enemy['x'], enemy['y']))


    pygame.display.flip()
    pygame
