import tkinter as tk, random  

#SnakeGUI==========================
# Purpose: represents the interface of the snake game
# Instance variables: (What are the instance variables for this class,
# win-sets up the tk instance
# canvas-tk instance reference
# board-the playing filed size/creation
# new_snake-creating the player controlled snake
# food_x-x position of food
# food_y-y position of food
# food_pellet-creating the food pellets (randomly
# enemy_snake-creating the computer controlled snake

# Methods:
# __init__ initilizes variables and sets up the playing field for the first time
# gameloop goes through each move of the game
# reset_game resets up the board/playing field when the game restarts
#==========================================

class SnakeGUI:
    def __init__(self):
        self.win=tk.Tk()
        self.canvas=tk.Canvas(self.win,width=660,height=660)
        self.canvas.pack()
        self.board=self.canvas.create_rectangle(30,30,630,630)
        self.new_snake=Snake(300,300,'green',self.canvas)
        self.food_x=random.randint(1, 20)*30
        self.food_y=random.randint(1, 20)*30
        self.food_pellet=self.canvas.create_oval(self.food_x,self.food_y,self.food_x+30,self.food_y+30,fill='red')
        self.win.bind('<Down>',self.new_snake.go_down)
        self.win.bind('<Up>',self.new_snake.go_up)
        self.win.bind('<Left>',self.new_snake.go_left)
        self.win.bind('<Right>',self.new_snake.go_right)
        self.enemy_snake=Snake(30,30,'red',self.canvas)
        self.gameloop()
    def gameloop(self):
        
        if self.new_snake.move(self.food_x,self.food_y) or self.enemy_snake.computer_move(self.food_x,self.food_y):
            self.canvas.delete(self.food_pellet)
            self.food_x=random.randint(1, 20)*30
            self.food_y=random.randint(1, 20)*30
            self.food_pellet=self.canvas.create_oval(self.food_x,self.food_y,self.food_x+30,self.food_y+30,fill='red')
        for i in self.new_snake.segments:
            for j in self.enemy_snake.segments:
                if self.canvas.coords(i)==self.canvas.coords(j):
                    self.new_snake.Gameover(len(self.new_snake.segments))
        if not self.new_snake.game_over:
            self.canvas.after(100,self.gameloop)
        else:
            self.bind_id=self.win.bind('r',self.reset_game)
    def reset_game(self,event):
        self.new_snake.game_over=True        
        self.canvas.delete(tk.ALL)
        self.board=self.canvas.create_rectangle(30,30,630,630)
        self.new_snake=Snake(300,330,'green',self.canvas)
        self.enemy_snake=Snake(30,30,'red',self.canvas)
        self.food_x=random.randint(1, 20)*30
        self.food_y=random.randint(1, 20)*30
        self.food_pellet=self.canvas.create_oval(self.food_x,self.food_y,self.food_x+30,self.food_y+30,fill='red')
        self.new_snake.game_over=False
        self.win.bind('<Down>',self.new_snake.go_down)
        self.win.bind('<Up>',self.new_snake.go_up)
        self.win.bind('<Left>',self.new_snake.go_left)
        self.win.bind('<Right>',self.new_snake.go_right)
        self.win.unbind('r',self.bind_id)
        self.gameloop()


#Snake===================================
# Purpose: all the snake information in terms of position, size, how to move, etc or the brains
# Instance variables: (What are the instance variables for this class,
# and what does each represent?)
# xpos the current x position of the snake
# ypos the current y position of the snake
# snake_color the color of the snake
# snake_name the name of the canvas object
# vx velocit of x
# vy velocity of y
# snake the current snake square that will be created and stored into segments
# game_over true false boolean to know if game is over
# x_dis distance from food to the computer (x)
# y_dis distance from food to computer (y)
# Methods: 
# move dictates how the player moves each turn
# go_down code to move player down
# go_up code to move player up
# go_right code to move player right
# go_left code to move player left
# Gameover sets game_over to true and prints the score
# computer_move dictaces how the comuter moves
#==========================================


class Snake:
    def __init__(self,xpos,ypos,snake_color,snake_name): 
        self.segments=[]
        self.xpos=xpos
        self.ypos=ypos
        self.vx=30
        self.vy=0  
        self.color=snake_color
        self.snake_name=snake_name
        self.snake=self.snake_name.create_rectangle(self.xpos,self.ypos,self.xpos+30,self.ypos+30,fill=self.color)
        self.segments=[self.snake]
    def move(self,food_x,food_y):
        self.game_over=False
        self.xpos+=self.vx
        self.ypos+=self.vy
        for i in self.segments:
            if self.xpos==self.snake_name.coords(i)[0] and self.ypos==self.snake_name.coords(i)[1]:
                self.Gameover(len(self.segments))
            if self.xpos>600 or self.xpos<30 or self.ypos>600 or self.ypos<30:
                self.Gameover(len(self.segments))
        self.segments.insert(0,self.snake_name.create_rectangle(self.xpos,self.ypos,self.xpos+30,self.ypos+30,fill=self.color))
        if food_x==self.xpos and food_y==self.ypos:
            return True
        else:
            self.snake_name.delete(self.segments.pop())
            return False
    def go_down(self,event):
        self.vx=0
        self.vy=30
    def go_up(self,event):
        self.vx=0
        self.vy=-30
    def go_right(self,event):
        self.vx=30
        self.vy=0
    def go_left(self,event):
        self.vx=-30
        self.vy=0
    def Gameover(self,score):
        self.game_over=True
        self.snake_name.create_text(300,300,text='Game over, final score:'+str(score))
    def computer_move(self,food_x,food_y):
        self.x_dis=food_x-self.xpos
        self.y_dis=food_y-self.ypos
        if self.x_dis**2>self.y_dis**2:
            if self.x_dis>0:
                self.xpos+=30
            else:
                self.xpos-=30
        else:
            if self.y_dis>0:
                self.ypos+=30
            else:
                self.ypos-=30
     
        self.game_over=False
        self.segments.insert(0,self.snake_name.create_rectangle(self.xpos,self.ypos,self.xpos+30,self.ypos+30,fill=self.color))
        if food_x==self.xpos and food_y==self.ypos:
            return True
        else:
            self.snake_name.delete(self.segments.pop())
            return False
SnakeGUI()
tk.mainloop()
