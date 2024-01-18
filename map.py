<<<<<<< HEAD
import pygame
import pytmx
import pyscroll

from screen import Screen

class Map:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.txm_data = None
        self.map_layer = None
        self.group = None
    
        self.switch_map("map")
    
    def switch_map(self, map: str):
        self.txm_data = pytmx.load_pygame(f"assets/decors/{map}.tmx")
        map_data = pyscroll.data.TiledMapData(self.txm_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)
        
    def uptade(self):
        self.group.draw(self.screen.get_display())
=======
import pygame
import pytmx
import pyscroll

from screen import Screen

class Map:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.txm_data = None
        self.map_layer = None
        self.group = None
    
        self.switch_map("map")
    
    def switch_map(self, map: str):
        self.txm_data = pytmx.load_pygame(f"assets/decors/{map}.tmx")
        map_data = pyscroll.data.TiledMapData(self.txm_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)
        
    def uptade(self):
        self.group.draw(self.screen.get_display())
>>>>>>> 0adbc4d4c15ec05d86043d72acc2396a33c0c20b
        