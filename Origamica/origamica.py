import pygame
import os
import random
from pygame.mixer import *
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
            
            x -= v
            fishimg = fish_left
      
            side = 0
    if key[pygame.K_UP] and y>=height-650:
            y -= v
    if key[pygame.K_DOWN] and y<=340:
            y += v
            
    #move by itself


    screen.blit(fishimg, (x,y))
    pygame.display.update()
    print(side)
    


pygame.quit()
