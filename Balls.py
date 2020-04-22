import pygame
import random
import math


pygame.init()

screen_x = 500
screen_y = 500
k_pos = [0, 0]
m_pos = [0, 0]
vv = [0, 0]
vv2 = [0, 0]
collision = 0
v_x = 0
v_y = 0
#параметры шара
radius = 20
wight = 20
x_b = int(screen_x / 2)
y_b = int(screen_y - radius - 20)
#x_b = random.randint(0 + radius, screen_x - radius)
#y_b = random.randint(0 + radius, screen_y - radius)
speed = 10
color_b = (2, 100, 135)


my_fond = pygame.font.SysFont('monospace', 15)
window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.Surface((screen_x, screen_y))

start_move = False
run = True


def move():
    global collision
    global x_b
    global y_b
    global v_x
    global v_y

    x_b += int(v_x)
    y_b += int(v_y)
    if x_b >= screen_x - radius or x_b <= 0 + radius:
        v_x = -v_x 
        collision += 1
    if y_b >= screen_y - radius or y_b <= 0 + radius:
        collision += 1
        v_y = -v_y
def vector():
    global v_x
    global v_y
    v_x_2 = k_pos[0] - x_b
    v_y_2 = k_pos[1] - y_b
    vv2[0] = v_x_2
    vv2[1] = v_y_2
    
    v_x = v_x_2 / math.sqrt((v_x_2**2 + v_y_2**2) / speed**2)
    v_y = v_y_2 / math.sqrt((v_x_2**2 + v_y_2**2) / speed**2)


    vv[0] = v_x
    vv[1] = v_y


while run:
    pygame.time.delay(15)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEMOTION:
                m_pos = e.pos
        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                k_pos = e.pos
                vector()
                start_move = True
                
    screen.fill((10, 50, 10))
    pygame.draw.circle(screen, color_b, (x_b, y_b), radius, wight)
    #string = my_fond.render('x = '+str(x_b) + ' y = ' + str(y_b), 0, (255, 0, 0))
    string = my_fond.render(str(vv2), 0, (255, 0, 0))
    string_2 = my_fond.render(str(vv), 0, (255, 0, 0))
    screen.blit(string, (0, 40))
    screen.blit(string_2, (200, 40))
    if start_move:
        move()
        if collision == 5:
            collision = 0
            x_b = int(screen_x / 2)
            y_b = int(screen_y - radius - 10)
            start_move = False
    window.blit(screen, (0, 0))
    pygame.display.update()
    #pygame.display.flip()
pygame.quit