import pygame

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DICE = [1]
ZOOM = 100
FONT = pygame.font.SysFont("monospace", int(ZOOM / 2))

screen = pygame.display.set_mode((len(DICE) * ZOOM, ZOOM))

c = pygame.time.Clock()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# SCREEN
	screen.fill(WHITE)
	for i in DICE:
		pygame.draw.rect(screen, BLACK, pygame.Rect(10, 10, 80, 80), 0, 20)
		text = "1"
		rendered = FONT.render(text, True, WHITE)
		screen.blit(rendered, (50 - (rendered.get_width() / 2), 50 - (rendered.get_height() / 2)))
	# FLIP
	pygame.display.flip()
	c.tick(60)
