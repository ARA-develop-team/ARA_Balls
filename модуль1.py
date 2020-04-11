import pygame
pygame.init()
FPS = 60
clock = pygame.time.Clock()
screenx = 500
screeny = 500
radius = 10
x_b = 100
y_b = 100
color_b = (100,100,100)
window = pygame.display.set_mode((screenx, screeny))
screen = pygame.Surface((screenx, screeny))
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color_b, (x_b, y_b), 50, 50)
    window.blit(screen, (0, 0))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
