import pygame # Importation de la bibliothèque Pygame
import random # Importation du module random pour choisir un Pokémon aléatoire
import json # Importation du module json pour charger les données des Pokémon

# Initialisation de Pygame
pygame.init()

# Initialisation de la fenêtre Pygame
largeur_fenetre = 1200 # Largeur de la fenêtre
hauteur_fenetre = 800 # Hauteur de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre)) # Création de la fenêtre
pygame.display.set_caption("Combat Pokémon") # Définition du titre de la fenêtre

# Chargement des données des Pokémon à partir du fichier JSON
with open('assets/pokemon/pokemon.json', encoding='utf-8') as pokemon_file:
   pokemon_data = json.load(pokemon_file)

class Combat: # Définition de la classe Combat

   def __init__(self): # Constructeur de la classe Combat
       self.pokemon_joueur = None # Pokémon du joueur
       self.pokemon_adversaire = None # Pokémon de l'adversaire

   def choisir_pokemon(self): # Méthode pour permettre au joueur de choisir un Pokémon
       choix = -1 # Initialisation du choix à -1
       font = pygame.font.Font(None, 36) # Création d'une police de caractères de taille 36

       while choix not in range(1, len(pokemon_data) + 1): # Boucle pour permettre au joueur de choisir un Pokémon valide
           fenetre.fill((255, 255, 255)) # Effacement de l'écran

           for i, pokemon in enumerate(pokemon_data): # Affichage des noms des Pokémon
               text_pokemon = font.render(f"{i + 1}. {pokemon['name']}", True, (0, 0, 0))
               fenetre.blit(text_pokemon, (50, 50 + i * 30))

           pygame.display.flip() # Actualisation de l'affichage

           try: # Essai de récupérer l'entrée clavier du joueur
               choix = str(input("Choisissez un Pokémon en entrant son nom : "))
           except ValueError: # Si l'entrée n'est pas un nombre
               choix = -1 # Réinitialisation du choix à -1

           if choix not in range(1, len(pokemon_data) + 1): # Si le choix est invalide
               print("Nom invalide. Veuillez choisir à nouveau.") # Affichage d'un message d'erreur

       self.pokemon_joueur = pokemon_data[choix - 1] # Définition du Pokémon du joueur
       self.pokemon_adversaire = random.choice(pokemon_data) # Définition du Pokémon de l'adversaire

   def afficher_combat(self): # Méthode pour afficher le message "Combat en cours..."
       fenetre.fill((255, 255, 255)) # Effacement de l'écran

       font = pygame.font.Font(None, 36) # Création d'une police de caractères de taille 36
       text_combat = font.render("Combat en cours...", True, (0, 0, 0)) # Création du texte "Combat en cours..."
       fenetre.blit(text_combat, (50, 150)) # Affichage du texte

       pygame.display.flip() # Actualisation de l'affichage

   def combat(self): # Méthode pour simuler le combat
       pygame.time.wait(2000) # Attente de 2 secondes pour simuler le combat

       fenetre.fill((255, 255, 255)) # Effacement de l'écran

       font = pygame.font.Font(None, 36) # Création d'une police de caractères de taille 36

       if random.choice([True, False]): # Détermination aléatoire du gagnant
           text_resultat = font.render("Vous avez gagné!", True, (0, 128, 0)) # Création du texte "Vous avez gagné!"
       else:
           text_resultat = font.render("Vous avez perdu!", True, (255, 0, 0)) # Création du texte "Vous avez perdu!"

       fenetre.blit(text_resultat, (50, 150)) # Affichage du texte
       pygame.display.flip() # Actualisation de l'affichage

# Instanciation d'un objet Combat
combat_instance = Combat()

# Boucle principale
while True:
   for event in pygame.event.get(): # Boucle pour gérer les événements
       if event.type == pygame.QUIT: # Si l'utilisateur ferme la fenêtre
           pygame.quit() # Quitter Pygame
           exit() # Quitter le programme

   # Laisser le joueur choisir un Pokémon au début du jeu
   if combat_instance.pokemon_joueur is None:
       combat_instance.choisir_pokemon() # Appel de la méthode choisir_pokemon()
       combat_instance.afficher_combat() # Appel de la méthode afficher_combat()
       combat_instance.combat() # Appel de la méthode combat()

   # Actualiser l'affichage
   pygame.display.flip() # Actualisation de l'affichage
   pygame.quit()
