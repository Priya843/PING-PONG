from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

paddle=Turtle()
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My PING PONG Game")
#this will turn on the animation
screen.tracer(0)
#these are like creating objects 
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()


#for right paddle
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
#for left paddle
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
#if you want to add any new paddle in screen incase 
#just do top_paddle call the Paddle class and pass on the position of x and y cor
#top_paddle=Paddle((180,180))

game_is_on=True
while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #detecting collision with the wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #datect collision with both paddles
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
    ball.bounce_x() 

  #datect when the ball misses the r_paddle 

  if ball.xcor() > 360:
    ball.reset_position()
    scoreboard.l_point()

  #same for l_paddle
  if ball.xcor() < -360:
    ball.reset_position()
    scoreboard.r_point()

  #keeping up with the score
  
    

screen.exitonclick()
