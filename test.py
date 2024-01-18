import pygame
import requests
import sys

pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Pokémon")

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

# Fonction pour afficher les données d'un Pokémon
def afficher_donnees_pokemon(pokemon):
    nom = pokemon["name"]["fr"]
    # Vérifier si la clé "types" est présente
    types = pokemon.get("types")

    if types is not None:
        # Récupérer uniquement les valeurs de la clé "name" des types
        type_names = [t.get("name", "") for t in types]
    else:
        type_names = []

    texte = font.render(f"Nom: {nom} - Types: {', '.join(type_names)}", True, (255, 255, 255))
    fenetre.blit(texte, (250, 250))

# Obtenir les données des Pokémon
donnees_pokemon = obtenir_donnees_pokemon()

# Index du Pokémon actuel
index_pokemon = 0

# Boucle principale du jeu
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  # Touche droite pour passer au Pokémon suivant
                index_pokemon = (index_pokemon + 1) % len(donnees_pokemon)
            elif event.key == pygame.K_LEFT:  # Touche gauche pour passer au Pokémon précédent
                index_pokemon = (index_pokemon - 1) % len(donnees_pokemon)

    fenetre.fill((0, 0, 0))

    # Afficher les données du Pokémon actuel dans la fenêtre
    afficher_donnees_pokemon(donnees_pokemon[index_pokemon])

    pygame.display.flip()

pygame.quit()
