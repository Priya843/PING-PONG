from turtle import Turtle
class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("pink")
    self.penup()
    self.goto(x=0,y=0)
    self.x_move = 10
    self.y_move = 10
    self.move_speed = 0.1
    #this means ball moves by 10 pixels and another 10 pixels 
  def move(self):
    new_x=self.xcor() + self.x_move 
    new_y=self.ycor() + self.y_move
    self.goto(new_x,new_y)

  # when the ball collides with up and bottom wall we gotta make the ball bounce back by subracting the ball move by 10 pixels everytime 
  def bounce_y(self):
    self.y_move *= -1
    
  #for collision with the r_paddle
  def bounce_x(self):
    self.x_move *= -1
    self.move_speed *= 0.9
  #for reseting the position of the ball when it misses r_paddle
  def reset_position(self):
    self.goto(0,0)
    move.move_speed=0.1
    self.bounce_x()

  #same for l_paddle
  