# -*- coding: utf-8 -*-
'''
MIT License

Copyright (c) 2024 JD edu. http://jdedu.kr author: conner.jeong@gmail.com
     
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
     
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
     
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN TH
SOFTWARE.
'''

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