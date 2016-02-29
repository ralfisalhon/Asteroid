import pygame
import time
from pygame.locals import *
from random import randint, randrange, uniform
from timeit import default_timer
pygame.init()

pygame.display.set_caption("Asteroid Game")

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

Width = 400
Height = 400
astCount = 50

y = 0
vel = 1

screen = pygame.display.set_mode((Width,Height))
back = pygame.Surface((Width,Height))
background = back.convert()
background.fill(black)
screen.blit(background,(0,0))

positions = []

for x in range(astCount):
	list = [randrange(0,Width), randrange(-10,10), randrange(-10000,-100), randrange(10,30)]
	positions.append(list)

print positions

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_q:
				exit()
	
	vel += 0.05
	y = y + vel

	screen.blit(background,(0,0))

	for x in range(astCount):
		pygame.draw.rect(screen, darkBlue, (positions[x][0] + (positions[x][1]*vel)/2, (y+positions[x][2])/20, positions[x][3], positions[x][3]), 0)
	
	pygame.display.update()