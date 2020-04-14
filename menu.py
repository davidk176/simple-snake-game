import pygame, time

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
        
    def display_game_over(self, game_window):
        font = pygame.font.SysFont('times new roman', 90)
        text = 'Game Over! Score: ' + str(self.score)
        surface = font.render(text, True, self.red)
        game_window.fill(self.black)
        game_window.blit(surface, (10, 10))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        
    