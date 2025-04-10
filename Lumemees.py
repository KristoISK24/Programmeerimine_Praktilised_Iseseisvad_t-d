import pygame
import sys

# Initsialiseeri Pygame
pygame.init()

# Loo aken (300x300) ja pane sellele nimi
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees - Kristo Arestov")

# Värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

# Tausta värv
screen.fill(BLACK)

# Joonista lumemees (3 valget ringi)
pygame.draw.circle(screen, WHITE, (150, 240), 50)  # alumine kehaosa
pygame.draw.circle(screen, WHITE, (150, 160), 40)  # keskmine kehaosa
pygame.draw.circle(screen, WHITE, (150, 90), 30)   # pea

# Silmad
pygame.draw.circle(screen, BLACK, (140, 80), 5)
pygame.draw.circle(screen, BLACK, (160, 80), 5)

# Nina (kolmnurk)
pygame.draw.polygon(screen, ORANGE, [(150, 90), (150, 100), (170, 95)])

# Uuenda ekraani
pygame.display.flip()

# Hoia aken avatuna, kuni kasutaja sulgeb selle
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
