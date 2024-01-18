import pygame
from screen import Screen

pygame.init()

class addPokemon:
    def __init__(self, nom, type, attaque, defense):
        self.__nom = nom
        self.__type = type
        self.__attaque = attaque
        self.__defense = defense
        self.__image = pygame.image.load("assets/pokemon/images/" + nom + ".png")


    def getNom(self):
        return self.__nom
    
    def getType(self):
        return self.__type
    
    def getAttaque(self):
        return self.__attaque
    
    def getDefense(self):
        return self.__defense
    
    def getImage(self):
        return self.__image
    
    def setNom(self, nom):
        self.__nom = nom

    def setType(self, type):
        self.__type = type
    
    def setAttaque(self, attaque):
        self.__attaque = attaque
    
    def setDefense(self, defense):
        self.__defense = defense
    
    def setImage(self, image):
        self.__image = image



