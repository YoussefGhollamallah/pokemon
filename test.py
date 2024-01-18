import pygame
import requests
import sys

pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Pokémon Viewer")

# Charger la police de caractères
font = pygame.font.Font(None, 20)

# Fonction pour obtenir les données des Pokémon depuis l'API
def obtenir_donnees_pokemon():
    url = "https://tyradex.vercel.app/api/v1/pokemon"
    try:
        reponse = requests.get(url)
        reponse.raise_for_status()
        donnees = reponse.json()
        return donnees  # La liste complète de Pokémon
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données : {e}")
        sys.exit(1)

# Fonction pour afficher les données des Pokémon
def afficher_donnees_pokemon(donnees, offset):
    y = 50
    for i, pokemon in enumerate(donnees):
        nom = pokemon["name"]["fr"]
         # Vérifier si la clé "types" est présente
        types = pokemon.get("types")
        
        if types is not None:
            # Récupérer uniquement les valeurs de la clé "name" des types
            type_names = [t.get("name", "") for t in types]
        else:
            type_names = []
        
        texte = font.render(f"{i + 1}. {nom} - Types: {', '.join(type_names)}", True, (255, 255, 255))
      
        fenetre.blit(texte, (50, y - offset))
        y += 30

# Obtenir les données des Pokémon
donnees_pokemon = obtenir_donnees_pokemon()

offset = 0
# Boucle principale du jeu
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:  # Molette vers le haut
            offset += 30
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:  # Molette vers le bas
            offset -= 30

    fenetre.fill((0, 0, 0))

    # Afficher les données des Pokémon dans la fenêtre
    afficher_donnees_pokemon(donnees_pokemon, offset)

    pygame.display.flip()

pygame.quit()
