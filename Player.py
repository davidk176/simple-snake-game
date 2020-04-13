
import pygame, sys, random

class Snake:
    head = [100, 50]
    body = [[100,50],[90,50],[80,50]]
    speed = 10
    direction = 'RIGHT'
    change_to = 'RIGHT'
    
    def get_body(self):
        return self.body
    
    def moveRight(self):
        self.x = self.x + self.speed
        
    def moveLeft(self):
        self.x = self.x - self.speed
        
    def moveUp(self):
        self.y = self.y + self.speed
        
    def moveDown(self):
        self.y = self.y -self.speed
        
    def change_direction(self):
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
            
    def move(self):
        if self.direction == 'UP':
            self.head[1] -= 10
        if self.direction == 'DOWN':
            self.head[1] += 10
        if self.direction == 'RIGHT':
            self.head[0] += 10
        if self.direction == 'LEFT':
            self.head[0] -= 10
            
        self.body.insert(0,list(self.head))
        self.body.pop(len(self.body)-1)[0]
        print("Moved to: " + self.direction)
        
class Food:
    elements = list()
    
    def __init__(self):
        #generate random food
        self.elements = [[300,400],[200,300],[10,10]]
        
    def spawn(self, frame_size_x, frame_size_y, snake):
        x = random.randrange(1, frame_size_x)
        y = random.randrange(1, frame_size_y)
        if x in snake.get_body()
            self.elements.append([x, y])
        
  
class Game:
    frame_size_x=1048
    frame_size_y=720
    snake = Snake()
    green = pygame.Color(0,255,0)
    black = pygame.Color(0,0,0)
    red = pygame.Color(255,0,0)
    food = Food()
    
    def get_Frame_Size(self):
        print("")
        
    #Do init      
    check_errors = pygame.init()
    if check_errors[1] > 0:
        print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
        sys.exit(-1)
    else:
        print('[+] Game successfully initialised')
    
    pygame.display.set_caption('Snake Game')
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
                    snake.change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    snake.change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    snake.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    snake.change_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                    
        snake.change_direction()
        snake.move()
        food.spawn(frame_size_x, frame_size_y, snake)
        game_window.fill(black)
        #Draw Snake
        for pos in snake.body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
        #Draw Food
        for e in food.elements:
            pygame.draw.rect(game_window, red, pygame.Rect(e[0], e[1], 10, 10))
            
        
        pygame.display.update()
        fps_controller.tick(snake.speed)
