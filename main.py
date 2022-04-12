import pygame
import random

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DICE = [1, 2, 3, 4, 5, 6]
ZOOM = 100
FONT = pygame.font.SysFont("monospace", int(ZOOM / 2))

screen = pygame.display.set_mode((len(DICE) * ZOOM, ZOOM))

def reroll():
	global DICE
	DICE = random.choices([1, 2, 3, 4, 5, 6], k=len(DICE))

reroll()

c = pygame.time.Clock()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONUP:
			reroll()
	# SCREEN
	screen.fill(WHITE)
	x = 0
	for i in DICE:
		pygame.draw.rect(screen, BLACK, pygame.Rect(x + 10, 10, 80, 80), 0, 20)
		rendered = FONT.render(str(i), True, WHITE)
		screen.blit(rendered, ((50 + x) - (rendered.get_width() / 2), 50 - (rendered.get_height() / 2)))
		x += 100
	# FLIP
	pygame.display.flip()
	c.tick(60)
