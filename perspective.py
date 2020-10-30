import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()

SURFACE = pygame.display.set_mode((1280,720))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Simulation")

class Object:
    l = 100     # length of the object (mm)
    d = 1000      #distance from the camera (mm)
    imagelength = (l / d) * 17
    def draw():
        pygame.draw.rect(SURFACE, (0,0,0), (640,360,2,round(Object.imagelength)))
    def text():
         font = pygame.font.Font(None, 32)
         text = font.render("Image length : "+str(Object.imagelength),True,(0,0,0))
         SURFACE.blit(text,(100,100))
def main():
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
         
        SURFACE.fill((255,255,255))

        key = pygame.key.get_pressed()
        
        if key[pygame.K_w]:
            pass
        elif key[pygame.K_s]:
            pass

        Object.draw()
        Object.text()
        
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()
