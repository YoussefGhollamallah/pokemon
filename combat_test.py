import pygame
import random
import json
import pygame_menu

# Initialiser la fenêtre Pygame
largeur_fenetre = 400
hauteur_fenetre = 300
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))


with open('../assets/pokemon/pokemon.json', encoding='utf-8') as pokemon:
    data = json.load(pokemon)

print(data)
class Combat:

    def afficher_pokemons(self):
        # Afficher la liste des pokemons disponibles
        options = [pokemon['name'] for pokemon in self.pokemon]
        y = 10
        for option in options:
            label = pygame.font.render(option, True, (255, 255, 255))
            pygame.display.get_surface().blit(label, (50, y))
            y += 30
            
    def player(): # permettre au joeur de choisir un element du fichier json avec une liste 
        player = player

    # def choisir_pokemon():
    #     pokemon_choisi = 
        
        # Attendre que le joueur fasse un choix
        choix_fait = False
        while not choix_fait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # La touche "Entrée" est pressée
                        choix_fait = True



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Actualiser l'affichage
    pygame.display.flip()
    pygame.quit()
    
    
# # Utilisation de la classe Combat
# pygame.init()
# pygame.display.set_mode((400, 300))
# combat = Combat()
# combat.afficher_pokemons()
# pygame.display.flip()
# pygame.time.delay(5000)  # Attendre 5 secondes avant de fermer la fenêtre
# pygame.quit()
