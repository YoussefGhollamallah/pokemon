import pygame

pygame.init()

class addPokemon:
    def __init__(self, nom, type, attaque, defense):
        self.nom = nom
        self.type = type
        self.attaque = attaque
        self.defense = defense

    def ajouterPokemon(self):
