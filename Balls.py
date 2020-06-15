import pygame
import random
import math


class Circle:
    def __init__(self, x_b, y_b):
        self.x_b = x_b
        self.y_b = y_b
        self.radius = 20
        self.wight = 20
        self.speed = 10
        self.color_b = (240, 230, 140)

    def vector(self, k_pos):
        v_x_2 = k_pos[0] - self.x_b
        v_y_2 = k_pos[1] - self.y_b

        v_x = v_x_2 / math.sqrt((v_x_2 ** 2 + v_y_2 ** 2) / self.speed ** 2)
        v_y = v_y_2 / math.sqrt((v_x_2 ** 2 + v_y_2 ** 2) / self.speed ** 2)

        return v_x, v_y

    def move(self, v_x, v_y, screen_x, screen_y):
        if self.x_b >= screen_x - self.radius or self.x_b <= 0 + self.radius:
            v_x = -v_x
            start_move = True
        if self.y_b <= 0 + self.radius:
            v_y = -v_y
            start_move = True
        if self.y_b >= screen_y - self.radius:
            start_move = False
        self.x_b += int(v_x)
        self.y_b += int(v_y)
        return start_move, self.x_b, self.y_b
    def draw_c(self, screen, x_b, y_b,):
        pygame.draw.circle(screen, self.color_b, (x_b, y_b), self.radius, self.wight)


class rect:
    def __init__(self, x_c, y_c):
        self.x_c = x_c
        self.y_c = y_c
        self.wight_c = 50
        self.height_c = 50
        self.color_c = (106, 90, 205)

pygame.init()
"""variable"""
screen_x = 500
screen_y = 500
radius = 20
start_move = False
run = True
ball = []
x_b = int(screen_x / 2)
y_b = int(screen_y - radius - 20)

my_fond = pygame.font.SysFont('monospace', 15)
window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.Surface((screen_x, screen_y))

for x in range(0, 4):
    ball.append(Circle(x_b, y_b))


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
                v_x, v_y = ball[0].vector(k_pos)
                print(v_x, v_y)
                start_move = True

    if start_move:
        for one in ball:
            start_move = True
            print('ok')
            start_move, x_b, y_b = one.move(v_x, v_y, screen_x, screen_y)
            one.draw_c(screen, x_b, y_b,)
    screen.fill((47, 79, 79))
    window.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit

# global start_move
# global collision
# global x_b
# global y_b
# global v_x
# global v_y
#
# screen_x = 500
# screen_y = 500
# k_pos = [0, 0]
# m_pos = [0, 0]
# vv = [0, 0]
# vv2 = [0, 0]
# collision = 0
# v_x = 0
# v_y = 0
#
# #парамтры квадрата
# x_c = 100
# y_c = 100
# wight_c = 50
# hight_c = 50
#
# #параметры шара
# radius = 20
# wight = 20
# x_b = int(screen_x / 2)
# y_b = int(screen_y - radius - 20)
# #x_b = random.randint(0 + radius, screen_x - radius)
# #y_b = random.randint(0 + radius, screen_y - radius)
# speed = 10
# color_b = (240, 230, 140)
#
#
#
#
# start_move = False
# run = True
#
#
# pygame.init()
# my_fond = pygame.font.SysFont('monospace', 15)
# window = pygame.display.set_mode((screen_x, screen_y))
# screen = pygame.Surface((screen_x, screen_y))
#
#
# def move():
#     global x_b
#     global y_b
#     global v_x
#     global v_y
#     global collision
#     global start_move
#     x_b += int(v_x)
#     y_b += int(v_y)
#     if x_b >= screen_x - radius or x_b <= 0 + radius:
#         v_x = -v_x
#         collision += 1
#     if y_b <= 0 + radius:
#         collision += 1
#         v_y = -v_y
#     if y_b >= screen_y - radius:
#         start_move = False
# def vector():
#     global v_x
#     global v_y
#     v_x_2 = k_pos[0] - x_b
#     v_y_2 = k_pos[1] - y_b
#     vv2[0] = v_x_2
#     vv2[1] = v_y_2
#
#     v_x = v_x_2 / math.sqrt((v_x_2**2 + v_y_2**2) / speed**2)
#     v_y = v_y_2 / math.sqrt((v_x_2**2 + v_y_2**2) / speed**2)
#
#
#     vv[0] = v_x
#     vv[1] = v_y
#
#
#
# while run:
#     pygame.time.delay(15)
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             run = False
#         if e.type == pygame.MOUSEMOTION:
#                 m_pos = e.pos
#         if e.type == pygame.MOUSEBUTTONUP:
#             if e.button == 1:
#                 k_pos = e.pos
#                 vector()
#                 start_move = True
#
#     screen.fill((47, 79, 79))
#     pygame.draw.circle(screen, color_b, (x_b, y_b), radius, wight)
#     pygame.draw.rect(screen, color_b, (x_c, y_c, wight_c, hight_c))
#     #string = my_fond.render('x = '+str(x_b) + ' y = ' + str(y_b), 0, (255, 0, 0))
#     string = my_fond.render(str(vv2), 0, (255, 0, 0))
#     string_2 = my_fond.render(str(vv), 0, (255, 0, 0))
#     screen.blit(string, (0, 40))
#     screen.blit(string_2, (200, 40))
#     if start_move:
#         move()
#         #if collision == 5:
#             #collision = 0
#             #start_move = False
#     window.blit(screen, (0, 0))
#     pygame.display.update()
#     #pygame.display.flip()
#
# pygame.quit
