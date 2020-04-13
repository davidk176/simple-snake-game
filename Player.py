
import pygame, sys, random, time

class Snake:
    head = [100, 50]
    body = [[100,50],[90,50],[80,50]]
    speed = 15
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
            
    def move(self, has_eaten):
        if self.direction == 'UP':
            self.head[1] -= 10
        if self.direction == 'DOWN':
            self.head[1] += 10
        if self.direction == 'RIGHT':
            self.head[0] += 10
        if self.direction == 'LEFT':
            self.head[0] -= 10
            
        self.body.insert(0,list(self.head))
        if not has_eaten:
            self.body.pop(len(self.body)-1)[0]
        else:
            print("Snake has eaten", has_eaten)
       # print("Moved to: " + self.direction)
        
    def eat(self, food):
        for fruit in food.elements:
            if self.head[0] == fruit[0] and self.head[1] == fruit[1]:
                print("head[0]",self.head[0])
                print("fruit[0]",fruit[0])
                food.elements.remove(fruit)
                print("Snake eats food")
                return True
        return False
                
    def check_collision(self):
        for part in self.body[1:]:
            if part[0] == self.head[0] and part[1] == self.head[1]:
                print("Snake eats body")
                return True
        return False
        
class Food:
    elements = list()
    amount = 1
    
    def __init__(self, frame_size_x, frame_size_y, amount):
        #generate random food
        self.amount = amount
        i=0
        
        while i < amount:
            x = (random.randrange(1, frame_size_x)//10)*10
            y = (random.randrange(1, frame_size_y)//10)*10

            if [x, y] not in self.elements:
                self.elements.append([x,y])
                i+=1
        
    def spawn(self, frame_size_x, frame_size_y, snake):
        x = (random.randrange(1, frame_size_x)//10)*10
        y = (random.randrange(1, frame_size_y)//10)*10
        
        if len(self.elements) < self.amount and [x,y] not in snake.get_body():
            self.elements.append([x, y])
        
  
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
    food = Food(frame_size_x, frame_size_y, amount_of_food)
    snake = Snake()
    
    has_eaten = False
    
    def get_Frame_Size(self):
        return [frame_size_x, frame_size_y]
    
        
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
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # on key is pressed down
            if event.type == pygame.KEYDOWN:
            #  WASD or arrow keys
                if event.key == pygame.K_UP or event.key == ord('w'):
                    snake.change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    snake.change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    snake.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    snake.change_to = 'RIGHT'
                # Esc -> exit
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        #change direction of snake
        snake.change_direction()
        
        has_eaten = snake.eat(food)
        #move snake
        snake.move(has_eaten)
        #spawn food
        food.spawn(frame_size_x, frame_size_y, snake)
        #check if snake eats body
        if snake.check_collision():
            font = pygame.font.SysFont('times new roman', 90)
            surface = my_font.render('YOU DIED', True, red)
            game_over_rect = game_over_surface.get_rect()
            game_window.fill(black)
            game_window.blit(game_over_surface, game_over_rect)
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
        game_window.fill(black)
        
        #Draw Snake
        for pos in snake.body:
        # Snake body
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
        #Draw Food
        for e in food.elements:
            pygame.draw.rect(game_window, red, pygame.Rect(e[0], e[1], 10, 10))
            
        
        pygame.display.update()
        fps_controller.tick(snake.speed)
