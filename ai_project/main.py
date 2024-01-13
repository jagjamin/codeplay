import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Galaga Clone")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 폰트 설정
font = pygame.font.Font(None, 36)

# 플레이어 설정
player_width, player_height = 30, 30
player_x = (width - player_width) // 2
player_y = height - player_height - 20
player_speed = 5

# 총알 설정
bullet_width, bullet_height = 5, 15
bullet_speed = 8
bullets = []
shoot_delay = 0

# 적 설정
enemy_width, enemy_height = 30, 30
enemy_speed = 2
enemies = []

# 목숨 설정
lives = 3
life_image = pygame.image.load("life.png")  # 목숨 이미지 불러오기
life_image = pygame.transform.scale(life_image, (20, 20))  # 이미지 크기 조절

# 점수 초기화
score = 0

# 시간 초기화
start_time = pygame.time.get_ticks()

# 적 생성 함수
def spawn_enemy():
    enemy_x = random.randint(0, width - enemy_width)
    enemy_y = random.randint(0, 100)
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
        enemy['alive'] = False  # 적의 alive 상태를 False로 설정
        spawn_enemy()
        increase_score()

# 목숨 표시 함수
def display_lives():
    for i in range(lives):
        life_rect = life_image.get_rect()
        life_rect.topleft = (width - (i + 1) * life_rect.width, 10)
        screen.blit(life_image, life_rect)

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    if keys[pygame.K_SPACE] and shoot_delay == 0:
        bullet_x = player_x + (player_width - bullet_width) // 2
        bullet_y = player_y
        bullets.append({'x': bullet_x, 'y': bullet_y})
        shoot_delay = 15

    if shoot_delay > 0:
        shoot_delay -= 1

    for bullet in bullets:
        bullet['y'] -= bullet_speed
        if bullet['y'] < 0:
            bullets.remove(bullet)

    for enemy in enemies[:]:
        for bullet in bullets[:]:
            handle_enemy_hit(bullet, enemy)
            if is_collision({'x': player_x, 'y': player_y}, enemy) and enemy['alive']:
                enemies.remove(enemy)
                spawn_enemy()
                lives -= 1
                if lives == 0:
                    print("게임 오버")
                    pygame.quit()
                    sys.exit()

    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000
    if elapsed_time > 0 and elapsed_time % 1 == 0:
        increase_score()
        start_time = current_time

    screen.fill(white)

    pygame.draw.rect(screen, (0, 0, 255), [player_x, player_y, player_width, player_height])

    for enemy in enemies:
        if enemy['alive']:
            pygame.draw.rect(screen, (255, 0, 0), [enemy['x'], enemy['y'], enemy_width, enemy_height])
            enemy['y'] += enemy_speed
            if enemy['y'] > height:
                enemy['alive'] = False
                spawn_enemy()

    for bullet in bullets:
        pygame.draw.rect(screen, (0, 255, 0), [bullet['x'], bullet['y'], bullet_width, bullet_height])

    display_lives()  # 목숨 표시 추가

    score_text = font.render("Score: {}".format(score), True, black)
    screen.blit(score_text, (width - 150, 30))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

    if random.randint(0, 100) < 2:
       
