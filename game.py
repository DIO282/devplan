import pygame

# 초기화
pygame.init()

# 게임 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("플레이어 움직임")

background = pygame.image.load("background.jpg")  # 이미지 파일 이름에 맞게 수정
# 색깔 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 플레이어 설정
player_size = 25
player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 0.1

# 플레이어 이동 함수
def move_player(keys, player_x, player_y, player_speed):
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < screen_width - player_size:
        player_x += player_speed
    if keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_s] and player_y < screen_height - player_size:
        player_y += player_speed
    return player_x, player_y

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_x, player_y = move_player(keys, player_x, player_y, player_speed)

    # 배경 이미지 그리기
    screen.blit(background, (0, 0))

    # 플레이어 그리기
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_size, player_size))

    pygame.display.update()

pygame.quit()