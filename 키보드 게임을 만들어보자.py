import pygame
import sys
from pygame.locals import*
import random
pygame.init()
SCREEN = pygame.display.set_mode((600,600))
CLOCK = pygame.time.Clock()


direc = ('up','down','left','right')

i = 0

cnt = 0

rec1 = 0
rec2 = 0
rec3 = 0
rec4 = 0

c1 = 0,255,0
c2 = 0,255,0
c3 = 0,255,0
c4 = 0,255,0
c5 = 0,255,0

sysfont = pygame.font.SysFont(None,36)
sysfont2 = pygame.font.SysFont(None,60)

u_txt = sysfont.render("up",True,(255,255,255))
d_txt = sysfont.render("down",True,(255,255,255))
l_txt = sysfont.render("left",True,(255,255,255))
r_txt = sysfont.render("right",True,(255,255,255))

while True :
    SCREEN.fill((255,255,255))
            
    cnt +=1
    if cnt >= 60:
        cnt=0
        i = random.randint(0,3)
    dr_txt= sysfont2.render(direc[i],True,(0,0,0))
    SCREEN.blit(dr_txt,(250,100))

    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

    if event.type == KEYDOWN:
            if event.key == K_UP:
                txt = sysfont.render("up",True,(0,0,0))
            if event.key == K_DOWN:
                txt = sysfont.render("down",True,(0,0,0))
            if event.key == K_RIGHT:
                txt = sysfont.render("right",True,(0,0,0))
            if event.key == K_LEFT:
                txt = sysfont.render("left",True,(0,0,0))

       
   
    pygame.display.update()
    CLOCK.tick(60)
                                                           
