import pygame 

pygame.init()

def play_sound(sound):
    pygame.mixer_music.load()
    music = pygame.mixer.Sound(sound)
    music.play(-1)
    play_sound('Battle.mp3')


class Musique:
    def combat(Musique):
        print("Combat de la musique")
   
       
        
    def victoire(Musique):
        print("Victoire de la musique !!!")

    def defaite(Musique):
        print("Défaite de la musique...")
        
    def ville(Musique):
        print( "musique La Ville")
    
    def hors_ville(Musique):
        print("musique hors ville")

pygame.quit()

