import pygame
from pygame import locals

pygame.init()

window = pygame.display.set_mode([500,500], vsync=1)


x = 250
y = 250

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


    window.fill((250,250,250))

    
    pygame.draw.circle(window, (100, 0, 255), (x, y), 75)
    pygame.display.flip()


pygame.quit()