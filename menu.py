import pygame
import sys
import os
import random
from screen import Screen
from test import *

class Menu(Screen):
    def __init__(self, background_images_directory):
        super().__init__()
        self.font = pygame.font.Font(None, 50)
        self.menu_items = ["Jouer", "Ajouter un Pokemon","Pokedex", "Quitter"]
        self.selected_item = 0

        
        self.background_images = [f for f in os.listdir(background_images_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        self.current_background = None

        
        self.change_background()

    def change_background(self):
        if self.background_images:
            background_image = random.choice(self.background_images)
            self.current_background = pygame.image.load(os.path.join(background_images_directory, background_image))
            

    def draw_menu(self):
        text_color = (0, 0, 0)
        selected_color = (255, 0, 0)

        
        if self.current_background:
            background_rect = self.current_background.get_rect(center=(self.get_size()[0] // 2, self.get_size()[1] // 2))
            self.get_display().blit(self.current_background, background_rect)

        for i, item in enumerate(self.menu_items):
            if i == self.selected_item:
                text = self.font.render(item, True, selected_color)
            else:
                text = self.font.render(item, True, text_color)

            text_rect = text.get_rect(center=(self.get_size()[0] // 2, 150 + i * 100))
            self.get_display().blit(text, text_rect)

    def run_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                    elif event.key == pygame.K_UP:
                        self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                    elif event.key == pygame.K_RETURN:
                        selected_action = self.menu_items[self.selected_item]
                        if selected_action == "Jouer":
                            print("Lancer le jeu")
                            # Ajoutez le code pour lancer le jeu ici
                        elif selected_action == "Pokedex":
                            print("Ouvrir le Pokedex")
                            app.run()
                        elif selected_action == "Ajouter un Pokemon":
                            print("Ajouter un Pokemon")
                            # Ajoutez le code pour ouvrir le Pokedex ici
                        elif selected_action == "Quitter":
                            pygame.quit()
                            sys.exit()
                        else:
                            self.change_background()  

            self.draw_menu()
            self.update()



background_images_directory = "assets/pokemon/images"
pygame.init()
menu = Menu(background_images_directory)

menu.run_menu()   