import random

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
        