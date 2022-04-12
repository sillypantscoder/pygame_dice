import pygame
import random

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DICE = [1, 2, 3, 4, 5, 6]
ZOOM = 100
FONT = pygame.font.SysFont("monospace", int(ZOOM / 2))
FONTHEIGHT = FONT.render("0", True, BLACK).get_height()
DICE_HEIGHT = 0
TEXTHEIGHT = 0

screen = pygame.display.set_mode((len(DICE) * ZOOM, ZOOM + FONTHEIGHT))

def reroll():
	global DICE
	global DICE_HEIGHT
	global TEXTHEIGHT
	DICE = random.choices([1, 2, 3, 4, 5, 6], k=len(DICE))
	DICE_HEIGHT = -ZOOM
	TEXTHEIGHT = FONTHEIGHT

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
		pygame.draw.rect(screen, BLACK, pygame.Rect(x + 10, 10 + DICE_HEIGHT, 80, 80), 0, 20)
		rendered = FONT.render(str(i), True, WHITE)
		screen.blit(rendered, ((50 + x) - (rendered.get_width() / 2), (50 + DICE_HEIGHT) - (rendered.get_height() / 2)))
		x += 100
	DICE_HEIGHT /= 1.1
	if DICE_HEIGHT >= -1: TEXTHEIGHT /= 1.6
	rendered = FONT.render("Total: " + str(sum(DICE)), True, BLACK)
	screen.blit(rendered, (0, 100 + TEXTHEIGHT))
	# FLIP
	pygame.display.flip()
	c.tick(60)
