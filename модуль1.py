import pygame
pygame.init()

rx=100
ry=100
widht1=20
height1=20

screenx = 500
screeny = 500
window = pygame.display.set_mode((screenx, screeny))
screen = pygame.Surface((screenx, screeny))

pygame.draw.rect(window, (255, 0, 0), (rx,ry,widht1,height1))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    screen.fill((0, 10, 0))
    window.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()


