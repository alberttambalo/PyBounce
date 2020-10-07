import pygame
import os
import time
import random
import math
from random import randint

WIDTH, HEIGHT = 750, 750

WIN = pygame.display.set_mode((WIDTH,HEIGHT))



class Ball:
    def __init__(self, x, y, r, g, b, i, j):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.i = i
        self.j = j
        self.bc = 0

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.slope = (y2-y1)/(x2-x1)
        print("SLOPE = " + str(self.slope))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    Balls = []
    Lines = []
    CLine = []

    def draw_back():
        WIN.fill((0,0,0))

    def draw_lines():
        for l in Lines:
            pygame.draw.line(WIN,(255,255,255), (l.x1,l.y1), (l.x2,l.y2), 10)

    def gravity_balls():
        for b in Balls:
            if b.j < 20:
                b.j = b.j + randint(0,1)


    def move_balls():
        for b in Balls:
            b.x = b.x + b.i
            b.y = b.y + b.j

    def draw_balls():
        for b in Balls:
            pygame.draw.circle(WIN, (b.r,b.g,b.b), (b.x,b.y), 10, 9)

    def check_collisions():
        for l in Lines:
            prec = 1000
            temp = []
            piecex = (l.x2 - l.x1) / prec
            piecey = (l.y2-l.y1) / prec
            segx = l.x1
            segy = l.y1
            for i in range(prec):
                segx = segx + piecex
                segy = segy + piecey
                temp.append((segx,segy))
            for t in temp:
                for b in Balls:

                    if 15 > math.sqrt((b.x - t[0])**2 + (b.y - t[1])**2):
                        #print(b.i)
                        #print(b.j)

                        #print(str(((1-(l.slope**2))/(1+((l.slope)**2))) + ((2 * l.slope)/(1 + (l.slope)**2))))
                        #print(str(((2 * l.slope)/(1+l.slope**2)) + (((l.slope**2)-1)/(1+l.slope**2))))
                        if l.slope > 0:
                             roll = 0
                        elif l.slope < 0:
                            roll =  0
                        else:
                            roll = 0

                        b.i = int(b.i * ((1-(l.slope**2))/(1+((l.slope)**2))) + ( b.j * ((2 * l.slope)/(1 + (l.slope)**2)))) + roll
                        b.j = int(b.i * ((2 * l.slope)/(1+l.slope**2)) + (b.j * (((l.slope**2)-1)/(1+l.slope**2))))

                        #print("TOUCHING " + str(b.i) + ", " + str(b.j))
                        colors = [(255,0,0),(0,255,0),(0,0,255)]

                        choose = colors[randint(0,2)]
                        b.r = choose[0]
                        b.g = choose[1]
                        b.b = choose[2]
                        for i in range(2):
                            b.x = b.x + b.i
                            b.y = b.y + b.j

    def clear_balls():
        for b in Balls:
            if b.x < 0 or b.x > WIDTH:
                Balls.remove(b)
            elif b.y < 0 or b.y > HEIGHT:
                Balls.remove(b)


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for i in range(5):
                        temp = Ball(randint(50,700),50,255,0,0,0,0)##randint(0,255),randint(0,255),randint(0,255),0,0)
                        Balls.append(temp)
                if event.key == pygame.K_c:
                    Balls.clear()
                if event.key == pygame.K_r:
                    Lines.clear()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                CLine.append((mx,my))
                if len(CLine) == 2:
                    line = Line(CLine[0][0],CLine[0][1],CLine[1][0],CLine[1][1])
                    Lines.append(line)
                    CLine.clear()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                mx, my = pygame.mouse.get_pos()
                CLine.append((mx,my))
                if len(CLine) == 2:
                    line = Line(CLine[0][0],CLine[0][1],CLine[1][0],CLine[0][1])
                    Lines.append(line)
                    CLine.clear()

        clear_balls()
        draw_back()
        draw_lines()
        draw_balls()
        check_collisions()
        move_balls()
        gravity_balls()



        pygame.display.update()

main()