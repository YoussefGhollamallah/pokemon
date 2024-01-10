import pygame,sys

pygame.init()

screen = pygame.display.set_mode((1300, 750))
pygame.display.set_caption("Poketmonster")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()


    screen.fill((25, 35, 55))
    pygame.display.flip()
    clock.tick(60)
