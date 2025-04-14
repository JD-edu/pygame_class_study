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
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("움직이는 파란 공과 떨어지는 빨간 공")

# 색상 정의
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# 파란 공 (우주선) 설정
spaceship_radius = 25  # 반지름 (지름 50 픽셀)
spaceship_x = screen_width // 2  # 초기 x 좌표 (화면 중앙)
spaceship_y = screen_height - spaceship_radius * 2  # 초기 y 좌표 (화면 하단)
spaceship_speed = 5  # 이동 속도

# 빨간 공 (적군) 설정
enemy_radius = 15  # 반지름 (지름 30 픽셀)
enemy_x = screen_width // 2  # 초기 x 좌표 (화면 중앙)
enemy_y = 0 - enemy_radius  # 초기 y 좌표 (화면 위쪽 바깥)
enemy_speed = 2  # 떨어지는 속도

# 프레임 레이트 설정
FPS = 30
clock = pygame.time.Clock()

# 게임 루프
running = True
while running:
    clock.tick(FPS)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 파란 공 (우주선) 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship_x -= spaceship_speed
        if spaceship_x < spaceship_radius:
            spaceship_x = spaceship_radius
    if keys[pygame.K_RIGHT]:
        spaceship_x += spaceship_speed
        if spaceship_x > screen_width - spaceship_radius:
            spaceship_x = screen_width - spaceship_radius

    # 빨간 공 (적군) 이동 및 위치 초기화
    enemy_y += enemy_speed
    if enemy_y > screen_height + enemy_radius:
        enemy_y = 0 - enemy_radius
        enemy_x = random.randint(enemy_radius, screen_width - enemy_radius)

    # 화면 그리기
    screen.fill(black)

    # 파란 공 (우주선) 그리기
    pygame.draw.circle(screen, blue, (spaceship_x, spaceship_y), spaceship_radius)

    # 빨간 공 (적군) 그리기
    pygame.draw.circle(screen, red, (enemy_x, int(enemy_y)), enemy_radius)

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()