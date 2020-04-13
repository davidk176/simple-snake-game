#Simple Snake Game
import pygame, sys, time, snake, food
  
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
        snake.move(has_eaten, frame_size_x, frame_size_y)
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

