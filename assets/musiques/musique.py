import pygame
import sys

pygame.display.set_caption("music pokemon")
window_resolution = (800, 600)
window = pygame.display.set_mode(window_resolution)
pygame.display.flip()

class Musique:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            'Opening': pygame.mixer.Sound("Opening.wav"),
            'Battle': pygame.mixer.Sound("Battle.wav"),
            'victoryT': pygame.mixer.Sound("victoryT.wav"),
            # 'defeat': pygame.mixer.Sound("defeat.mp3"),
            'City': pygame.mixer.Sound("City.wav"),
            # 'out_of_city': pygame.mixer.Sound("out_of_city.mp3")
        }

    def accueil(self):
        self.sounds['Opening'].play()

    def combat(self):
        print("Combat de la musique")
        self.play_sound('Battle')

    def victoire(self):
        print("Victoire de la musique !!!")
        self.play_sound('victoryT')

    # def defaite(self):
    #     print("Défaite de la musique...")
    #     self.play_sound('defeat')

    def ville(self):
        print("musique La Ville")
        self.play_sound('City')

    # def hors_ville(self):
    #     print("musique hors ville")
    #     self.play_sound('out_of_city')

    def play_sound(self, sound_name):
        self.sounds[sound_name].play()

# Exemple d'utilisation :
musique_instance = Musique()
musique_instance.accueil()

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Votre logique de jeu ici

    pygame.display.update()
