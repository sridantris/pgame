import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Hello World! - MY NAME :Sri Dantris')

while True:
	for event in pygame.event.get():
	if event.type == QUIT;
	pygame.display.update()