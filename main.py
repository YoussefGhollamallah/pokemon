import pygame
import random
from menu import *

pygame.init()

if __name__ == "__main__":
    while True:
     
        menu.run_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()