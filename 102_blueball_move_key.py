import pygame

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("움직이는 파란 공")

# 색상 정의
blue = (0, 0, 255)
black = (0, 0, 0)

# 공 설정
ball_radius = 25  # 반지름 (지름 50 픽셀)
ball_x = screen_width // 2  # 초기 x 좌표 (화면 중앙)
ball_y = screen_height - ball_radius * 2  # 초기 y 좌표 (화면 하단)
ball_speed = 5  # 이동 속도

# 프레임 레이트 설정 (원하는 속도에 맞춰 조절)
FPS = 30  # 초당 프레임 수

# 게임 루프
running = True
clock = pygame.time.Clock()  # Pygame 시계 객체 생성

while running:
    # 프레임 레이트 조절
    clock.tick(FPS)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed
        if ball_x < ball_radius:  # 화면 왼쪽 경계 처리
            ball_x = ball_radius
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed
        if ball_x > screen_width - ball_radius:  # 화면 오른쪽 경계 처리
            ball_x = screen_width - ball_radius

    # 화면 그리기
    screen.fill(black)
    pygame.draw.circle(screen, blue, (ball_x, ball_y), ball_radius)

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()