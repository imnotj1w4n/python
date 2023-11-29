import sys
import pygame
from pygame.locals import *
import random

pygame.init()
SCREEN = pygame.display.set_mode((600, 600))
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 72)

# 이미지 로드 - light_img(번개 이미지), man_img(사람 이미지)
light_img = pygame.image.load("light.png")
man_img = pygame.image.load("man.png")

# 이미지의 크기를 알려주는 함수
l_size = light_img.get_size()
m_size = man_img.get_size()

# 사람 이미지 좌표 초기화
m_x, m_y = 250, 480

# 번개 이미지의 좌표를 저장할 빈 리스트
l_x = []
l_y = []

# 번개 생성 시간 컨트롤 위한 변수 초기화
cnt = 0

# 게임 종료 판정 변수 초기화
game_over = False

while True :
    # 충돌되면 게임 중단
    if game_over :
        break

    # 화면을 검정색으로 채운다
    SCREEN.fill((0, 0, 0))
    
    for event in pygame.event.get() :
        # 창 닫기 버튼 누르면 종료
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

    """ 번개의 x, y 좌표 리스트에 추가(1초에 3번) """
    # [x 좌표] 랜덤으로 생성하여 번개 이미지의 x 좌표 리스트에 추가
    # [y 좌표] 0으로 하여  번개 이미지의 x 좌표 리스트에 추가
    cnt += 1
    if cnt >= 20 :
        cnt = 0
        l_x.append(random.randint(0, 600))
        l_y.append(0)

    """ 번개 출력 """
    for i in range(len(l_x)) :
        # 번개가 5씩 아래로 내려옴
        l_y[i] += 5
        # 번개를 화면에 출력
        SCREEN.blit(light_img, (l_x[i], l_y[i]))
        # 번개가 바닥에 떨어지면 떨어진 번개 이미지, x, y 좌표 삭제 
        if l_y[i] >= 550 :
            l_x.remove(l_x[i])
            l_y.remove(l_y[i])
            break

    """ 좌우 키를 누르면 사람 이미지를 해당 방향으로 5씩 이동 """
    key_event = pygame.key.get_pressed() 
    if key_event[pygame.K_LEFT]:
        if m_x > 0:			
            m_x -= 5
    if key_event[pygame.K_RIGHT]:
        if m_x < 500:
            m_x += 5
            
    # 사람 이미지 화면에 출력    
    SCREEN.blit(man_img, (m_x, m_y))       
    
    """ 충돌 감지 """
    # 번개 이미지와 사람 이미지가 겹치면 화면에 'Game Over!' 출력하고
    # game_over 변수값 True로 변경
    for i in range(len(l_x)) :
        if l_x[i] + l_size[0] >= m_x  and m_x + m_size[0] >= l_x[i] :
            if l_y[i] - l_size[1] >= m_y : 
                msg = sysfont.render("Game Over!", True, (255,0,0))
                SCREEN.blit(msg, (160, 250)) 
                game_over = True
               
    pygame.display.update()
    CLOCK.tick(60)

# 게임 종료 후에 창 닫기 버튼 누면 종료
while True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
