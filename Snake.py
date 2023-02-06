
import keyboard
import random
import time


class Snake:
    """
    TO DO:
    - Add scoring system 
    - Make more fluid
    - Add play again feature
    """
    def __init__(self, width = 10, height = 10):
        self.__border = [width,height]
        self.__body = [[int(self.__border[0]/2), int(self.__border[1]/2)]] # SET AT THE MIDDLE OF MAP
        self.__alive = True
        self.__direction = [1,0]
        self.__initial = True
        self.__map = [[]] * height
        self.__food = None
       
    def move (self, direction):
        # CHECK IF ALIVE
        position = [self.__body[0][0] + direction[1], self.__body[0][1] + direction[0]]
        if self.is_alive():
           
            at_wall = self.__at_wall(self.__body[0]) 
            
            #not_at_tail = (self.__body.get_end() != position)
            at_self = position in self.__body # and not_at_tail  
            
            if at_self or at_wall: 
                self.__die()
            # AT FOOD    
            elif self.__body[0] == self.__food:
                self.__eat(self.__food)
                self.__create_food()
            # KEEP MOVING
            else:
                self.__body.insert(0,position)
                self.__body.pop()
    
    def __eat (self, position):
        self.__body.insert(0, position)
    
    def is_alive(self):
        return self.__alive
    
    def __die(self):
        self.__alive = False
        
    def __at_wall(self, position):

        if position[0] == 0 or position[0] == self.__border[0] -1 or position[1] == 0 or position[1] == self.__border[1] -1:
            return True
        return False
        
    def __create_food(self):
        x = 0
        y = 0
        random_spot = [x,y]
        while self.__map[x][y] != ' ':
            x = random.randint(1, self.__border[0] - 1)
            y = random.randint(1, self.__border[1] - 1)
        
        random_spot = [x,y]            
        self.__food = random_spot
        
    def __get_direction(self):
        #key = keyboard.read_key()
        if keyboard.is_pressed('up'):      # UP
            self.__direction = [0,-1] 
        elif keyboard.is_pressed('down'):  # DOWN
            self.__direction = [0,1]
        elif keyboard.is_pressed('left'):  # LEFT
            self.__direction = [-1,0]
        elif keyboard.is_pressed('right'): # RIGHT
            self.__direction = [1,0]
            
        return self.__direction
            

    def __draw(self):

        print("\n")
        
        # CREATE MAP
        self.__map = []
        for x in range(self.__border[0]):     # ROW
            counter = 0 
            self.__map.append([])
            for y in range(self.__border[1]): # COLUMN
                #print(x,y)
                if self.__at_wall( (x,y) ):   # CREATE BORDER
                    self.__map[x].append('#') 
                else:
                    self.__map[x].append(' ') # BLANK REST        
        
        if self.__initial: 
            self.__initial = False            
            self.__create_food()      
            
        # DRAW SNAKE
        for xy in self.__body:
            if xy != None: 
                if xy == self.__body[0]:
                    self.__map[xy[0]][xy[1]] = 'O'
                else:
                    self.__map[xy[0]][xy[1]] = 'o'
                
        # DRAW FOOD
        self.__map[self.__food[0]][self.__food[1]] = '*'
        
        # PRINT ALL
        for height in self.__map:
            row = ""
            for i in height:
                row += i + " "
            print(row)

    def run(self):
        while self.is_alive():
            self.__draw()
            self.__get_direction()
            self.move(self.__direction)
            time.sleep(0.4)
            self.__get_direction()
            
def main():
    game = Snake()
    game.run()

if __name__=='__main__':
    main()           

