import pygame
import time
import math
"""variable"""
screen_x = 500
screen_y = 500
balls = []
vv = [0, 0]
radius = 1
color_b = (240, 230, 140)
speed = 10
number = 200   #количество шариков
x_b = int(screen_x/2)
y_b = screen_y - radius - 1
v_x = 0
v_y = 0
a = 0
timing = 0

run = True
start_move = False
balls_run = False

window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.Surface((screen_x, screen_y))


class Circle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = int(vx)
        self.vy = int(vy)
    def move(self):
        if self.x >= screen_x - radius or self.x <= 0 + radius:
            self.vx = -self.vx
        if self.y <= 0 + radius or self.y >= screen_y - radius:
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy
        pygame.draw.circle(screen, color_b, (self.x, self.y), radius, radius)
def vector():
     v_x_2 = k_pos[0] - x_b
     v_y_2 = k_pos[1] - y_b

     v_x = v_x_2 / math.sqrt((v_x_2**2 + v_y_2**2) / speed**2)
     v_y = v_y_2 / math.sqrt((v_x_2**2 + v_y_2**2) / speed**2)

     return v_x, v_y
pygame.init()
while run:
    pygame.time.delay(15)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEBUTTONUP:
             if e.button == 1:
                 k_pos = e.pos
                 v_x, v_y = vector()
                 for x in range(0, number):
                    balls.append(Circle(x_b, y_b, v_x, v_y))
                 timing = time.time()
                 start_move = True
                 balls_run = True
    screen.fill((47, 79, 79))
    if time.time() - timing > 0.2 and balls_run:
        a += 1
        if a == number:
            balls_run = False
        timing = time.time()
    if start_move:
        for x in range(0, a):
            balls[x].move() 
    window.blit(screen, (0, 0))
    pygame.display.update()

pygame.quit

