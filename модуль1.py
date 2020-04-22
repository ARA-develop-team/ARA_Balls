import pygame

#def check_cube (xz, yz, rx, ry,):

#def check_sq (xz, yz, rx, ry, ):

pygame.init()
FPS = 60
clock = pygame.time.Clock()
rx=100
ry=100
widht1=20
height1=20
screenx = 500
screeny = 500
radius = 10
x_b = 100
y_b = 100
color_b = (100,100,100)
window = pygame.display.set_mode((screenx, screeny))
screen = pygame.Surface((screenx, screeny))

num = 20
actioin = False

#pygame.draw.rect(window, (255, 0, 0), (rx,ry,widht1,height1))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color_b, (x_b, y_b), 50, 50)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        action = True

   # if  check_cube (xz, yz, rx, ry,) = True
        num -= 1



    screen.fill((0, 10, 0))
    window.blit(screen, (0, 0))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
