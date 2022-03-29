import pygame
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LENGTH = 12000
WIDTH = 6000
screen = pygame.display.set_mode((LENGTH, WIDTH))
gameExit = False
gameLoop = True
for x in range(-20000, 10001):
    for y in range(-10000, 10001):
        j = complex(0, 0)
        for i in range(100):
            z = j**2 + complex(x/10000, y/10000)
            j = z
            if abs(z) > 2:
                pygame.draw.circle(screen, (i, i, i), (x/(30000/LENGTH) + 2*LENGTH/3, WIDTH/2 - y/(20000/WIDTH)), 1)
                break
        else:
            pygame.draw.circle(screen, BLACK, (x/(30000/LENGTH) + 2*LENGTH/3, WIDTH/2 - y/(20000/WIDTH)), 1)
pygame.display.update()
f_string = f"Mandelset.jpeg"
pygame.image.save(screen, f_string)
exit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f_string = f"Mandelset.jpeg"
            pygame.image.save(screen, f_string)
            exit()
    pygame.display.update()
