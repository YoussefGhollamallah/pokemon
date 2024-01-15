<<<<<<< HEAD
import pygame


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((1200, 720))
        pygame.display.set_caption("Pokémon")
        self.clock = pygame.time.Clock()
        self.framerate = 60

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.framerate)
        self.display.fill((0, 0, 0))

    def get_size(self):
        return self.display.get_size()

    def get_display(self):
=======
import pygame


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((1200, 720))
        pygame.display.set_caption("Pokémon")
        self.clock = pygame.time.Clock()
        self.framerate = 60

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.framerate)
        self.display.fill((0, 0, 0))

    def get_size(self):
        return self.display.get_size()

    def get_display(self):
>>>>>>> 0adbc4d4c15ec05d86043d72acc2396a33c0c20b
        return self.display