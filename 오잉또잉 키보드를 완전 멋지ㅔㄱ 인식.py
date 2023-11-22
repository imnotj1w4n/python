import pygame
import sys
from pygame.locals import*

pygame.init()
SCREEN = pygame.display.set_mode((300,300))
CLOCK = pygame.time.Clock()
# b,w
BLACK = (0,0,0)
WHITE =(255,255,255)

sysfont = pygame.font.SysFont(None,36)

txt = sysfont.render("",True,BLACK)

while True :
    SCREEN.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
            
        if event.type == KEYDOWN:
            if event.key == K_UP:
                txt = sysfont.render("up",True,BLACK)
            if event.key == K_DOWN:
                txt = sysfont.render("down",True,BLACK)
            if event.key == K_RIGHT:
                txt = sysfont.render("right",True,BLACK)
            if event.key == K_LEFT:
                txt = sysfont.render("left",True,BLACK)
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    SCREEN.blit(txt,(100,120))
    pygame.display.update()
    CLOCK.tick(60)
