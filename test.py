import pygame
import requests
import sys

class ListPokemon:
    def __init__(self):
        pygame.init()

        self.largeur, self.hauteur = 800, 600
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Pokémon")

        self.font = pygame.font.Font(None, 20)


        self.donnees_pokemon = self.obtenir_donnees_pokemon()

        self.index_pokemon = 0

   
    def obtenir_donnees_pokemon(self):
        url = "https://tyradex.vercel.app/api/v1/pokemon"
        try:
            reponse = requests.get(url)
            reponse.raise_for_status()
            donnees = reponse.json()
            return donnees
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la récupération des données : {e}")
            sys.exit(1)


    def afficher_donnees_pokemon(self, pokemon):
        nom = pokemon["name"]["fr"]

        types = pokemon.get("types")

        if types is not None:
            type_names = [t.get("name", "") for t in types]
        else:
            type_names = []

        texte = self.font.render(f"Nom: {nom} - Types: {', '.join(type_names)}", True, (255, 255, 255))
        self.fenetre.blit(texte, (250, 250))


    def run(self):
        en_cours = True
        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.index_pokemon = (self.index_pokemon + 1) % len(self.donnees_pokemon)
                    elif event.key == pygame.K_LEFT:
                        self.index_pokemon = (self.index_pokemon - 1) % len(self.donnees_pokemon)

            self.fenetre.fill((0, 0, 0))

            self.afficher_donnees_pokemon(self.donnees_pokemon[self.index_pokemon])

            pygame.display.flip()

        pygame.quit()


app = ListPokemon()

