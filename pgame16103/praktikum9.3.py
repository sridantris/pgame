import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480)) #x-y
done = False
warna_bg = (240,24, 55)

pygame.display.set_caption ("Hallo My World")


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and \
	event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_bg)
	pygame.draw.line(screen, (0, 0, 255), (0, 0), (400, 300), 5)
	pygame.draw.line(screen, (255, 255, 255), (400,300), (640, 480), 5)
	#pygame.draw.rect(screen, (0, 255, 255), (100,100,300,200), 3)

	pygame.display.flip()