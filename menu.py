import pygame

class Menu:
    score = 0
    
    #Colors
    green = pygame.Color(0,255,0)
    black = pygame.Color(0,0,0)
    red = pygame.Color(255,0,0)
    
    def __init__(self):
        self.score = 0
        
    def display_score(self, game_window):
        font = pygame.font.SysFont('arial', 35)
        surface = font.render('Score : ' + str(self.score), True, self.red)
        game_window.blit(surface, (10, 10))
        
    def increment_score(self):
        self.score += 1
        
    