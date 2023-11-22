import pygame
import sys
from pygame.locals import*

pygame.init()
SURFACE = pygame.display.set_mode((300,300))
CLOCK = pygame.time.Clock()
# r,g,b
BLACK = (0,0,0)
WHITE =(255,255,255)
RED =(255,0,0)
GREEN =(0,255,0)
BLUE =(0,0,255)

while True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    SURFACE.fill(WHITE)

    rec = Rect(20,10,60,40)
    
    pygame.draw.circle(SURFACE,GREEN,(150,150),150)
    
    pygame.draw.rect(SURFACE,BLUE,(50,50,200,200))

    pygame.draw.rect(SURFACE,RED,(100,100,100,100))


    pygame.draw.polygon(SURFACE,BLACK,[[200,200],[200,100],[100,100]])
    
   

    pygame.display.update()
    CLOCK.tick(1)
