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
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=[]
                self.desavantage=['Rock', 'Spectre']
                self.egal=['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Dark', 'Dragon', 'Steel', 'Fairy']


class Fire(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Grass', 'Ice', 'Bug', 'Steel']
                self.desavantage=['Water', 'Rock', 'Dragon']
                self.egal=['Normal', 'Fire', 'Electric', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Spectre', 'Dark', 'Fairy']     


class Water(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type, hp,attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Fire', 'Ground', 'Rock']
                self.desavantage=['Grass', 'Dragon']
                self.egal=['Normal', 'Water', 'Electric', 'Ice', 'Fighting', 'Poison', 'Flying', 'Psychic', 'Bug', 'Spectre', 'Dark', 'Steel', 'Fairy']


class Grass(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type, hp,attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Water', 'Ground', 'Rock']
                self.desavantage=['Fire', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']
                self.egal=['Normal', 'Grass', 'Electric', 'Ice', 'Fighting', 'Psychic', 'Spectre', 'Dark', 'Fairy']


class Electric(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Water', 'Flying']
                self.desavantage=['Grass', 'Ground', 'Dragon']
                self.egal=['Normal', 'Fire', 'Electric', 'Ice', 'Fighting', 'Poison', 'Psychic', 'Bug', 'Rock', 'Spectre', 'Dark', 'Steel', 'Fairy']


class Ice(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Grass', 'Ground', 'Flying', 'Dragon']
                self.desavantage=['Fire', 'Water', 'Steel']
                self.egal=['Normal', 'Electric', 'Ice', 'Fighting', 'Poison', 'Psychic', 'Bug', 'Rock', 'Spectre', 'Dark', 'Fairy']


class Fighting(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Normal', 'Ice', 'Rock', 'Dark', 'Steel']
                self.desavantage=['Poison', 'Flying', 'Psychic', 'Bug', 'Spectre', 'Fairy']
                self.egal=['Fire', 'Water', 'Grass', 'Electric', 'Fighting', 'Ground', 'Dragon']


class Poison(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Grass', 'Fairy']
                self.desavantage=['Ground', 'Rock', 'Spectre', 'Steel']
                self.egal=['Normal', 'Fire', 'Water', 'Electric', 'Ice', 'Fighting', 'Poison', 'Flying', 'Psychic', 'Bug', 'Dark', 'Dragon']  


class Ground(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Fire', 'Electric', 'Poison', 'Rock', 'Steel']
                self.desavantage=['Grass', 'Flying', 'Bug']
                self.egal=['Normal', 'Water', 'Ice', 'Fighting', 'Ground', 'Psychic', 'Spectre', 'Dark', 'Dragon', 'Fairy']


class Flying(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type, hp,attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Grass', 'Fighting', 'Bug']
                self.desavantage=['Electric', 'Rock', 'Steel']
                self.egal=['Normal', 'Fire', 'Water', 'Ice', 'Poison', 'Ground', 'Flying', 'Psychic', 'Spectre', 'Dark', 'Dragon', 'Fairy']  


class Psychic(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Fighting', 'Poison']
                self.desavantage=['Dark', 'Steel']
                self.egal=['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Spectre', 'Dragon', 'Fairy']


class Bug(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Grass', 'Psychic', 'Dark']
                self.desavantage=['Fire', 'Fighting', 'Poison', 'Flying', 'Spectre', 'Steel', 'Fairy']
                self.egal=['Normal', 'Water', 'Electric', 'Ice', 'Ground', 'Bug', 'Rock', 'Dragon']


class Rock(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Fire', 'Ice', 'Flying']
                self.desavantage=['Fighting', 'Ground', 'Steel']
                self.egal=['Normal', 'Water', 'Grass', 'Electric', 'Poison', 'Psychic', 'Bug', 'Rock', 'Spectre', 'Dark', 'Dragon', 'Fairy']

class Spectre(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type, hp,attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Psychic']
                self.desavantage=['Normal', 'Dark']
                self.egal=['Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Bug', 'Rock', 'Spectre', 'Dragon', 'Steel', 'Fairy']


class Dark(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Psychic', 'Spectre']
                self.desavantage=['Fighting', 'Fairy']
                self.egal=['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Poison', 'Ground', 'Flying', 'Bug', 'Rock', 'Dark', 'Dragon', 'Steel']


class Dragon(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=[]
                self.desavantage=['Steel', 'Fairy']
                self.egal=['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Spectre', 'Dark', 'Dragon']


class Steel(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type, hp,attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Ice', 'Rock', 'Fairy']
                self.desavantage=['Fire', 'Water', 'Electric']
                self.egal=['Normal', 'Grass', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Spectre', 'Dark', 'Dragon', 'Steel']


class Fairy(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse, IVA ,IVD):
                super().__init__(nom, type,hp, attaque, defense, vitesse, IVA ,IVD)
                self.avantage=['Fighting', 'Dark', 'Dragon']
                self.desavantage=['Fire', 'Poison', 'Steel']
                self.egal=['Normal', 'Water', 'Grass', 'Electric', 'Ice', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Spectre', 'Fairy']  

import json

with open('pokedex.json', encoding='utf-8-sig') as f:
 data = json.load(f)
print(data)

