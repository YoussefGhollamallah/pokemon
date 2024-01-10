import random
import math

class Pokemon:
        def __init__(self,id ,nom ,type ,hp ,attaque ,defense , vitesse,IVA ,IVD):
                self.nom = nom
                self.type = type
                self.hp = hp
                self.attaque = attaque
                self.defense = defense
                self.vitesse = vitesse
                self.id  = id
                self.IVA = IVA
                self.IVD = IVD


        def calculavantage(self, opps):
                if opps.type.__name__ in self.avantage:
                        return 1.75
                
                elif opps.type.__name__  in self.desavantage:
                        return 0.5
                
                elif opps.type.__name__  in self.egal:
                        return 1
                


        

class Normal(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=[]
                self.desavantage=['Roche', 'Spectre']
                self.egal=['Normal', 'Feu', 'Eau', 'Plante', 'Electrique', 'Gel', 'Combat', 'Poison', 'Sol', 'Vol', 'Psy', 'Insecte', 'Tenebres', 'Dragon', 'Acier', 'Fee']


class Feu(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Plante', 'Gel', 'Insecte', 'Acier']
                self.desavantage=['Eau', 'Roche', 'Dragon']
                self.egal=['Normal', 'Feu', 'Electrique', 'Combat', 'Poison', 'Sol', 'Vol', 'Psy', 'Spectre', 'Tenebres', 'Fee']     


class Eau(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type, hp,attaque, defense, vitesse)
                self.avantage=['Feu', 'Sol', 'Roche']
                self.desavantage=['Plante', 'Dragon']
                self.egal=['Normal', 'Eau', 'Electrique', 'Gel', 'Combat', 'Poison', 'Vol', 'Psy', 'Insecte', 'Spectre', 'Tenebres', 'Acier', 'Fee']


class Plante(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type, hp,attaque, defense, vitesse)
                self.avantage=['Eau', 'Sol', 'Roche']
                self.desavantage=['Feu', 'Poison', 'Vol', 'Insecte', 'Dragon', 'Acier']
                self.egal=['Normal', 'Plante', 'Electrique', 'Gel', 'Combat', 'Psy', 'Spectre', 'Tenebres', 'Fee']


class Electrique(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Eau', 'Vol']
                self.desavantage=['Plante', 'Sol', 'Dragon']
                self.egal=['Normal', 'Feu', 'Electrique', 'Gel', 'Combat', 'Poison', 'Psy', 'Insecte', 'Roche', 'Spectre', 'Tenebres', 'Acier', 'Fee']


class Gel(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Plante', 'Sol', 'Vol', 'Dragon']
                self.desavantage=['Feu', 'Eau', 'Acier']
                self.egal=['Normal', 'Electrique', 'Gel', 'Combat', 'Poison', 'Psy', 'Insecte', 'Roche', 'Spectre', 'Tenebres', 'Fee']


class Combat(Pokemon):
        def __init__(self, nom, tipo, hp, attaque, defense, vitesse):
                super().__init__(nom, tipo,hp, attaque, defense, vitesse)
                self.avantage=['Normal', 'Gelo', 'Roche', 'Tenebres', 'Acier']
                self.desavantage=['Poison', 'Vol', 'Psy', 'Insecte', 'Spectre', 'Fee']
                self.egal=['Feu', 'Eau', 'Plante', 'Electrique', 'Combat', 'Sol', 'Dragon']


class Poison(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Plante', 'Fee']
                self.desavantage=['Sol', 'Roche', 'Spectre', 'Acier']
                self.egal=['Normal', 'Feu', 'Eau', 'Electrique', 'Gel', 'Combat', 'Poison', 'Vol', 'Psy', 'Insecte', 'Tenebres', 'Dragon']  


class Sol(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Feu', 'Electrique', 'Poison', 'Roche', 'Acier']
                self.desavantage=['Plante', 'Vol', 'Insecte']
                self.egal=['Normal', 'Eau', 'Gelo', 'Combat', 'Sol', 'Psy', 'Spectre', 'Tenebres', 'Dragon', 'Fee']


class Vol(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type, hp,attaque, defense, vitesse)
                self.avantage=['Plante', 'Combat', 'Insecte']
                self.desavantage=['Electrique', 'Roche', 'Acier']
                self.egal=['Normal', 'Feu', 'Eau', 'Gelo', 'Poison', 'Sol', 'Vol', 'Psy', 'Spectre', 'Tenebres', 'Dragon', 'Fee']  


class Psy(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Combat', 'Poison']
                self.desavantage=['Tenebres', 'Acier']
                self.egal=['Normal', 'Feu', 'Eau', 'Plante', 'Electrique', 'Gelo', 'Sol', 'Vol', 'Psy', 'Insecte', 'Roche', 'Spectre', 'Dragon', 'Fee']


class Insecte(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Plante', 'Psy', 'Tenebres']
                self.desavantage=['Feu', 'Combat', 'Poison', 'Vol', 'Spectre', 'Acier', 'Fee']
                self.egal=['Normal', 'Eau', 'Electrique', 'Gel', 'Sol', 'Insecte', 'Roche', 'Dragon']


class Roche(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Feu', 'Gel', 'Vol']
                self.desavantage=['Combat', 'Sol', 'Acier']
                self.egal=['Normal', 'Eau', 'Plante', 'Electrique', 'Poison', 'Psy', 'Insecte', 'Roche', 'Spectre', 'Tenebres', 'Dragon', 'Fee']

class Spectre(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type, hp,attaque, defense, vitesse)
                self.avantage=['Psy']
                self.desavantage=['Normal', 'Tenebres']
                self.egal=['Feu', 'Eau', 'Plante', 'Electrique', 'Gel', 'Combat', 'Poison', 'Sol', 'Vol', 'Insecte', 'Roche', 'Spectre', 'Dragon', 'Acier', 'Fee']


class Tenebres(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Psy', 'Spectre']
                self.desavantage=['Combat', 'Fee']
                self.egal=['Normal', 'Feu', 'Eau', 'Plante', 'Electrique', 'Gel', 'Poison', 'Sol', 'Vol', 'Insecte', 'Roche', 'Tenebres', 'Dragon', 'Acier']


class Dragon(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=[]
                self.desavantage=['Acier', 'Fee']
                self.egal=['Normal', 'Feu', 'Eau', 'Plante', 'Electrique', 'Gel', 'Combat', 'Poison', 'Sol', 'Vol', 'Psy', 'Insecte', 'Roche', 'Spectre', 'Tenebres', 'Dragon']


class Acier(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type, hp,attaque, defense, vitesse)
                self.avantage=['Gel', 'Roche', 'Fee']
                self.desavantage=['Feu', 'Eau', 'Electrique']
                self.egal=['Normal', 'Plante', 'Combat', 'Poison', 'Sol', 'Vol', 'Psy', 'Insecte', 'Spectre', 'Tenebres', 'Dragon', 'Acier']


class Fee(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Combat', 'Tenebres', 'Dragon']
                self.desavantage=['Feu', 'Poison', 'Acier']
                self.egal=['Normal', 'Eau', 'Plante', 'Electrique', 'Gel', 'Sol', 'Vol', 'Psy', 'Insecte', 'Roche', 'Spectre', 'Fee']  

import json

with open('pokedex.json', encoding='utf-8-sig') as f:
 data = json.load(f)
print(data)
