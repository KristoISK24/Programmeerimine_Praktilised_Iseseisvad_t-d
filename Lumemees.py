>>> import pygame
pygame 2.6.1 (SDL 2.28.4, Python 3.13.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
>>> import sys
>>>
>>> # Initsialiseeri Pygame
>>> pygame.init()
(5, 0)
>>>
>>> # Loo aken (300x300) ja pane sellele nimi
>>> screen = pygame.display.set_mode((300, 300))
>>> pygame.display.set_caption("Lumemees - Karin Eegreid")
>>>
>>> # Värvid
>>> WHITE = (255, 255, 255)
>>> BLACK = (0, 0, 0)
>>> ORANGE = (255, 165, 0)
>>>
>>> # Tausta värv
>>> screen.fill(BLACK)
<rect(0, 0, 300, 300)>
>>>
>>> # Joonista lumemees (3 valget ringi)
>>> pygame.draw.circle(screen, WHITE, (150, 240), 50)  # alumine kehaosa
<rect(100, 190, 100, 100)>
>>> pygame.draw.circle(screen, WHITE, (150, 160), 40)  # keskmine kehaosa
<rect(110, 120, 80, 80)>
>>> pygame.draw.circle(screen, WHITE, (150, 90), 30)   # pea
<rect(120, 60, 60, 60)>
>>>
>>> # Silmad
>>> pygame.draw.circle(screen, BLACK, (140, 80), 5)
<rect(135, 75, 10, 10)>
>>> pygame.draw.circle(screen, BLACK, (160, 80), 5)
<rect(155, 75, 10, 10)>
>>>
>>> # Nina (kolmnurk)
>>> pygame.draw.polygon(screen, ORANGE, [(150, 90), (150, 100), (170, 95)])
<rect(150, 90, 21, 11)>
>>>
>>> # Uuenda ekraani
>>> pygame.display.flip()
>>>
>>> # Hoia aken avatuna, kuni kasutaja sulgeb selle
>>> while True:
...         for event in pygame.event.get():
...                         if event.type == pygame.QUIT:
...                                             pygame.quit()
...                                                         sys.exit()