import pygame
pygame.init()
 
pygame.display.set_caption("pokemon")
 
surfaceW = 800 #Dimension de la fenêtre / Largeur
surfaceH = 600 #Dimension de la fenêtre / Longueur
 
 
screen = pygame.display.set_mode((surfaceW,surfaceH)) #Taille Ecran
myfont = pygame.font.SysFont('Helvetic', 20)
 
noir = (0,0,0) 
game_over = False #Le Programme tourne normalement 

    #Fermeture de la fenêtre
  

  
while not game_over: #Tant qu'il tourne = NP
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Si l'événement de Pygame qui s'execute est égale au boutton rouge X
                game_over= True   #La page se ferme
 
        screen.fill(noir) #Fond écran en noir
        pygame.display.update() #rafraichissement du fond
        

 
 
 

pygame.quit()
quit()