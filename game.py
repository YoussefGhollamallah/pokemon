<<<<<<< HEAD
import pygame
from screen import Screen
from map import Map

class Game:
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.map = Map(self.screen)
        
    def run(self):
        while self.running:
            self.map.uptade()
            self.screen.update()
=======
import pygame
from screen import Screen
from map import Map

class Game:
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.map = Map(self.screen)
        
    def run(self):
        while self.running:
            self.map.uptade()
            self.screen.update()
>>>>>>> 0adbc4d4c15ec05d86043d72acc2396a33c0c20b
