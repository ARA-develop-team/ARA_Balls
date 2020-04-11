import pygame
pygame.init()
screenx = 500
screeny = 500
window = pygame.display.set_mode((screenx, screeny))
screen = pygame.Surface((screenx, screeny))
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    screen.fill((0, 10, 0))
    window.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()


