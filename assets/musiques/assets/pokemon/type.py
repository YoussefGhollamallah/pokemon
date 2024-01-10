import random

class Pokemon:
        def __init__(self,nom,type,hp,attaque,defense, vitesse):
                self.nom = nom
                self.type = type
                self.hp = hp
                self.attaque = attaque
                self.defense = defense
                self.vitesse = vitesse


        def calculavantage(self, opps):
                if opps.type.__name__ in self.avantage:
                        return 2
                
                elif opps.type.__name__  in self.desavantage:
                        return 0.5
                
                elif opps.type.__name__  in self.egal:
                        return 1


        

class Normal(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=[]
                self.desavantage=['Roche', 'Fantasma']
                self.egal=['Normal', 'Feu', 'Eau', 'Plante', 'Electrique', 'Gel', 'Combattant', 'Venimeu', 'Terrestre', 'Vol', 'Psy', 'Insecte', 'Tenebres', 'Dragon', 'Acier', 'Fee']


class Feu(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Plante', 'Gel', 'Insecte', 'Acier']
                self.desavantage=['Eau', 'Roche', 'Dragon']
                self.egal=['Normal', 'Feu', 'Electrique', 'Combattant', 'Venimeu', 'Terrestre', 'Vol', 'Psy', 'Fantasma', 'Tenebres', 'Fee']     


class Eau(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type, hp,attaque, defense, vitesse)
                self.avantage=['Feu', 'Terrestre', 'Roche']
                self.desavantage=['Plante', 'Dragon']
                self.egal=['Normal', 'Eau', 'Electrique', 'Gel', 'Combattant', 'Venimeu', 'Vol', 'Psy', 'Insecte', 'Fantasma', 'Tenebres', 'Acier', 'Fee']


class Plante(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type, hp,attaque, defense, vitesse)
                self.avantage=['Eau', 'Terrestre', 'Roche']
                self.desavantage=['Feu', 'Venimeu', 'Vol', 'Insecte', 'Dragon', 'Acier']
                self.egal=['Normal', 'Plante', 'Electrique', 'Gel', 'Combattant', 'Psy', 'Fantasma', 'Tenebres', 'Fee']


class Electrique(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Eau', 'Vol']
                self.desavantage=['Plante', 'Terrestre', 'Dragon']
                self.egal=['Normal', 'Feu', 'Electrique', 'Gel', 'Combattant', 'Venimeu', 'Psy', 'Insecte', 'Roche', 'Fantasma', 'Tenebres', 'Acier', 'Fee']


class Gel(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Plante', 'Terrestre', 'Vol', 'Dragon']
                self.desavantage=['Feu', 'Eau', 'Acier']
                self.egal=['Normal', 'Electrique', 'Gel', 'Combattant', 'Venimeu', 'Psy', 'Insecte', 'Roche', 'Fantasma', 'Tenebres', 'Fee']


class Combattant(Pokemon):
        def __init__(self, nom, tipo, hp, attaque, defense, vitesse):
                super().__init__(nom, tipo,hp, attaque, defense, vitesse)
                self.avantage=['Normal', 'Gelo', 'Roche', 'Tenebres', 'Acier']
                self.desavantage=['Venimeu', 'Vol', 'Psy', 'Insecte', 'Fantasma', 'Fee']
                self.egal=['Feu', 'Eau', 'Plante', 'Electrique', 'Combattant', 'Terrestre', 'Dragon']


class Venimeu(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Plante', 'Fee']
                self.desavantage=['Terrestre', 'Roche', 'Fantasma', 'Acier']
                self.egal=['Normal', 'Feu', 'Eau', 'Electrique', 'Gel', 'Combattant', 'Venimeu', 'Vol', 'Psy', 'Insecte', 'Tenebres', 'Dragon']  


class Terrestre(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Feu', 'Electrique', 'Venimeu', 'Roche', 'Acier']
                self.desavantage=['Plante', 'Vol', 'Insecte']
                self.egal=['Normal', 'Eau', 'Gelo', 'Combattant', 'Terrestre', 'Psy', 'Fantasma', 'Tenebres', 'Dragon', 'Fee']


class Vol(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type, hp,attaque, defense, vitesse)
                self.avantage=['Plante', 'Combattant', 'Insecte']
                self.desavantage=['Electrique', 'Roche', 'Acier']
                self.egal=['Normal', 'Feu', 'Eau', 'Gelo', 'Venimeu', 'Terrestre', 'Vol', 'Psy', 'Fantasma', 'Tenebres', 'Dragon', 'Fee']  


class Psy(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Combattant', 'Venimeu']
                self.desavantage=['Tenebres', 'Acier']
                self.egal=['Normal', 'Feu', 'Eau', 'Plante', 'Electrique', 'Gelo', 'Terrestre', 'Vol', 'Psy', 'Insecte', 'Roche', 'Fantasma', 'Dragon', 'Fee']


class Insecte(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Plante', 'Psy', 'Tenebres']
                self.desavantage=['Feu', 'Combattant', 'Venimeu', 'Vol', 'Fantasma', 'Acier', 'Fee']
                self.egal=['Normal', 'Eau', 'Electrique', 'Gel', 'Terrestre', 'Insecte', 'Roche', 'Dragon']


class Roche(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Feu', 'Gel', 'Vol']
                self.desavantage=['Combattant', 'Terrestre', 'Acier']
                self.egal=['Normal', 'Eau', 'Plante', 'Electrique', 'Venimeu', 'Psy', 'Insecte', 'Roche', 'Fantasma', 'Tenebres', 'Dragon', 'Fee']

class Fantasma(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type, hp,attaque, defense, vitesse)
                self.avantage=['Psy']
                self.desavantage=['Normal', 'Tenebres']
                self.egal=['Feu', 'Eau', 'Plante', 'Electrique', 'Gel', 'Combattant', 'Venimeu', 'Terrestre', 'Vol', 'Insecte', 'Roche', 'Fantasma', 'Dragon', 'Acier', 'Fee']


class Tenebres(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Psy', 'Fantasma']
                self.desavantage=['Combattant', 'Fee']
                self.egal=['Normal', 'Feu', 'Eau', 'Plante', 'Electrique', 'Gel', 'Venimeu', 'Terrestre', 'Vol', 'Insecte', 'Roche', 'Tenebres', 'Dragon', 'Acier']


class Dragon(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=[]
                self.desavantage=['Acier', 'Fee']
                self.egal=['Normal', 'Feu', 'Eau', 'Plante', 'Electrique', 'Gel', 'Combattant', 'Venimeu', 'Terrestre', 'Vol', 'Psy', 'Insecte', 'Roche', 'Fantasma', 'Tenebres', 'Dragon']


class Acier(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type, hp,attaque, defense, vitesse)
                self.avantage=['Gel', 'Roche', 'Fee']
                self.desavantage=['Feu', 'Eau', 'Electrique']
                self.egal=['Normal', 'Plante', 'Combattant', 'Venimeu', 'Terrestre', 'Vol', 'Psy', 'Insecte', 'Fantasma', 'Tenebres', 'Dragon', 'Acier']


class Fee(Pokemon):
        def __init__(self, nom, type, hp, attaque, defense, vitesse):
                super().__init__(nom, type,hp, attaque, defense, vitesse)
                self.avantage=['Combattant', 'Tenebres', 'Dragon']
                self.desavantage=['Feu', 'Venimeu', 'Acier']
                self.egal=['Normal', 'Eau', 'Plante', 'Electrique', 'Gel', 'Terrestre', 'Vol', 'Psy', 'Insecte', 'Roche', 'Fantasma', 'Fee']  

 
pikachu = (Electrique)("pikachu",Electrique,35,40,55,90)
Tortipouss =(Plante)("Tortipouss",Plante,55,68,64,31)
Ouisticram = (Feu)("Ouisticram",Feu,44,58,44,61)
Tiplouf = (Eau)("Tiplouf",Feu,53,51,53,40)


pokemons = [pikachu, Tortipouss, Ouisticram, Tiplouf ]
starter = [Tortipouss, Ouisticram, Tiplouf]
