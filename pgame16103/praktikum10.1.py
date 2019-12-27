import pygame

running = 1
widht, height = 600, 400
x,y = 0,0
screen = pygame.display.set_mode((widht, height))
img = pygame.image.load('bola.png')
bg = pygame.image.load("bg.png").convert()
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	if event.type == pygame.KEYDOWN and \
	event.key == pygame.K_ESCAPE:
		running = 0

	screen.blit (bg, [0,0])
	screen.blit(img, [x+20, y+50])
	pygame.display.flip()