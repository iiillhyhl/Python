#가장 긴 변이 나머지 두 변을 합한 것보다 작아야 한다.
import pygame
import random
import sys
import math
from pygame.locals import QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN
pygame.init()
SURFACE = pygame.display.set_mode((500,500))
FPSCLOCK = pygame.time.Clock()
class Grid:
    def draw():
        x = pygame.draw.line(SURFACE,(0,0,0),(250,0),(250,500))
        y = pygame.draw.line(SURFACE,(0,0,0),(0,250),(500,250))

def coords(a,b):
    return (250+5*a, 250-5*b)
def main():
    a,b,c = map(int, input('a >= b >= c 순으로 입력').split())
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:   # key bindings
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))
        Grid.draw()
        A = pygame.draw.line(SURFACE,(255,0,0),coords(0,0),coords(a,0),2)
        c1 = pygame.draw.circle(SURFACE,(0,0,255),coords(0,0),b*5,2)
        c2 = pygame.draw.circle(SURFACE,(0,0,255),coords(50,0),c*5,2)
        px = (math.pow(a,2) - math.pow(c,2))/a
        px = int(px)
        l = pygame.draw.line(SURFACE,(0,255,0),coords(px,50),coords(px,-50),2)
        py = int((b**2 - px**2)**0.5)
        B = pygame.draw.line(SURFACE,(255,0,0),coords(0,0),coords(px,py),2)
        C = pygame.draw.line(SURFACE,(255,0,0),coords(px,py),coords(a,0),2)
        FPSCLOCK.tick(10)
            
        pygame.display.update()


if __name__ == '__main__':
    main()
