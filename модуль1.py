import pygame

def check_cube (xz, yz, rx, ry,):

def check_sq (xz, yz, rx, ry, ):

pygame.init()
screenx = 500
screeny = 500
window = pygame.display.set_mode((screenx, screeny))
screen = pygame.Surface((screenx, screeny))
num = 20
actioin = False
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        action = True

    if  check_cube (xz, yz, rx, ry,) = True
        num -= 1



    screen.fill((0, 10, 0))
    window.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()


