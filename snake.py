class Snake:
    head = [100, 50]
    body = [[100,50],[90,50],[80,50]]
    speed = 15
    direction = 'RIGHT'
    change_to = 'RIGHT'
    
    def get_body(self):
        return self.body
    
    def change_direction(self):
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
            
    def move(self, has_eaten, x, y):
        if self.direction == 'UP':
            self.head[1] = (self.head[1] - 10) % y
        if self.direction == 'DOWN':
            self.head[1] = (self.head[1] + 10) % y
        if self.direction == 'RIGHT':
            self.head[0] = (self.head[0] + 10) % x
        if self.direction == 'LEFT':
            self.head[0] = (self.head[0] - 10) % x
            
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
        