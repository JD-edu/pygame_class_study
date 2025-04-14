import pygame

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("파란 공 그리기")

# 색상 정의
blue = (0, 0, 255)
black = (0, 0, 0)

# 공 설정
ball_radius = 25  # 반지름 (지름 50 픽셀)
ball_x = screen_width // 2  # 화면 중앙의 x 좌표
ball_y = screen_height // 2 # 화면 중앙의 y 좌표

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 그리기
    screen.fill(black)  # 배경을 검은색으로 채우기
    pygame.draw.circle(screen, blue, (ball_x, ball_y), ball_radius)

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()