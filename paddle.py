from turtle import Turtle
class Paddle(Turtle):
  def __init__(self,position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid=5,stretch_len=1)
    self.penup()
    self.goto(position)
    #for moving up and down 
  def go_up(self):
    new_y=self.ycor() + 20
    self.goto(self.x_cor(),new_y)
  
  def go_down(self):
    new_y=self.ycor() - 20
    self.goto(self.x_cor(),new_y)
      
    
    
  
    
  
  
 
    

#below code for moving paddle up and down 
