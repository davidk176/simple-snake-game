
import pygame, sys

class Player:
    x = 10;
    y = 10
    speed = 1
    
    def moveRight(self):
        self.x = self.x + self.speed
        
    def moveLeft(self):
        self.x = self.x - self.speed
        
    def moveUp(self):
        self.y = self.y + self.speed
        
    def moveDown(self):
        self.y = self.y -self.speed
  
class Game:
    frame_size_x=1048
    frame_size_y=720
    
    #Do init      
    check_errors = pygame.init()
    if check_errors[1] > 0:
        print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
        sys.exit(-1)
    else:
        print('[+] Game successfully initialised')
    
    pygame.display.set_caption('Snake Eater')
    game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
    fps_controller = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Whenever a key is pressed down
            if event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
