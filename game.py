#Simple Snake Game
import pygame, sys, time, snake, food, menu
  
class Game:
    #Init Frame Size
    frame_size_x=1048
    frame_size_y=720
    
    #Colors
    green = pygame.Color(0,255,0)
    black = pygame.Color(0,0,0)
    red = pygame.Color(255,0,0)
    
    #Game objects
    amount_of_food = 10
    food = food.Food(frame_size_x, frame_size_y, amount_of_food)
    snake = snake.Snake()
    menu = menu.Menu()
    score = 0
    
    has_eaten = False
    
    #Start Game logic with init     
    check_errors = pygame.init()
    if check_errors[1] > 0:
        print(f'[!] Error while initialising game')
        sys.exit(-1)
    else:
        print('[+] Game successfully initialised')
    
    pygame.display.set_caption('Snake Game')
    game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
    fps_controller = pygame.time.Clock()
    
    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # on key is pressed down
                if event.type == pygame.KEYDOWN:
                #  WASD or arrow keys
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        self.snake.change_to = 'UP'
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        self.snake.change_to = 'DOWN'
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        self.snake.change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        self.snake.change_to = 'RIGHT'
                    # Esc -> exit
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))
            #change direction of snake
            self.snake.change_direction()
            
            self.has_eaten = self.snake.eat(self.food)
            if self.has_eaten:
                self.menu.increment_score()
            #move snake
            self.snake.move(self.has_eaten, self.frame_size_x, self.frame_size_y)
            #spawn food
            self.food.spawn(self.frame_size_x, self.frame_size_y, self.snake)
            self.game_window.fill(self.black)
            #check if snake eats body
            if self.snake.check_collision():
                font = pygame.font.SysFont('times new roman', 90)
                surface = font.render('YOU DIED', True, self.red)
                rect = surface.get_rect()
                self.game_window.fill(self.black)
                self.game_window.blit(surface, rect)
                pygame.display.flip()
                time.sleep(3)
                pygame.quit()
            #Draw Snake
            for pos in self.snake.body:
            # Snake body
                pygame.draw.rect(self.game_window, self.green, pygame.Rect(pos[0], pos[1], 10, 10))
            
            #Draw Food
            for e in self.food.elements:
                pygame.draw.rect(self.game_window, self.red, pygame.Rect(e[0], e[1], 10, 10))
                
            #font = pygame.font.SysFont('arial', 20)
            #surface = font.render('Score : ' + str(self.score), True, self.red)
            #self.game_window.blit(surface, (100, 100))
            self.menu.display_score(self.game_window)    
                
            pygame.display.update()
            self.fps_controller.tick(self.snake.speed)
    
    
if __name__ == "__main__":
    game= Game()
    game.start_game()
    

