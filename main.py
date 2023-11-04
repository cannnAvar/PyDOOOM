import pygame
from pygame import locals
import player

pygame.init()

window = pygame.display.set_mode([500,500], vsync=1)



pl = player.Player(100, 100)


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


    window.fill((250,250,250))

    pl.draw(window)

    pygame.display.flip()


pygame.quit()