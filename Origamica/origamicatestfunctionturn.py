import pygame
import os
import random

pygame.init()

# Basic Variables
fps = 100
width = 800
height = 600
sprites = []
black = (0,0,0)
white = (255, 255, 255)

x = 400
y = 200
v = 10

current = 1
side = 1
sideframe = 10
turnleft = False
turnright = False


fish_left = pygame.image.load("l_motion0.png")
fish_right = pygame.image.load("r_motion0.png")
turn1 = pygame.image.load("turn1.png")
turn2 = pygame.image.load("turn2.png")
turn3 = pygame.image.load("turn3.png")
turn4 = pygame.image.load("turn4.png")
turn5 = pygame.image.load("turn5.png")
turn6 = pygame.image.load("turn6.png")
turn7 = pygame.image.load("turn7.png")
turn8 = pygame.image.load("turn8.png")
turn9 = pygame.image.load("turn9.png")
turn10 = pygame.image.load("turn10.png")
fishimg = pygame.image.load("r_motion0.png") 


class You:
    def __init__(self):
        self = pygame.sprite.Sprite()
        self.image = fishimg
        self.rect = self.image.get_rect()
        outline = self.image.get_rect()
        self.rect.center = [x,y]
        w = outline[2]
        h = outline[3]

      
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Origamica")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((0, 255, 120))
    fish = You()

    key = pygame.key.get_pressed() 

    if key[pygame.K_RIGHT] and x < width - 319:
            
            x += v
            fishimg = fish_right
            side = 1


    if key[pygame.K_LEFT] and x > -100:
            while True:
                if sideframe == 10:
                    fishimg = turn1
                if sideframe == 20:
                    fishimg = turn2
                if sideframe == 30:
                    fishimg = turn3
                if sideframe == 40:
                    fishimg = turn4
                if sideframe == 50:
                    fishimg = turn5
                if sideframe == 60:
                    fishimg = turn6
                if sideframe == 70:
                    fishimg = turn7
                if sideframe == 80:
                    fishimg = turn8
                if sideframe == 90:
                    fishimg = turn9
                if sideframe == 100:
                    fishimg = turn10
                    sideframe = 1
                    break
                else:
                    sideframe += 1
                    continue
           
            side = 0 

        
            x -= v
                #fishimg = fish_left
                
            
            
    if key[pygame.K_UP] and y > -52:
            y -= v
    if key[pygame.K_DOWN] and y < height - 250:
            y += v
    
    screen.blit(fishimg, (x,y))
    pygame.display.update()
    print(sideframe)
    


pygame.quit()
