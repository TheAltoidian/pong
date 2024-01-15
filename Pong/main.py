from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep

screen = Screen()
screen.setup(width=1200, height=650)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


L_paddle = Paddle()
R_paddle = Paddle()
L_paddle.start_left()
R_paddle.start_right()
ball = Ball()

screen.listen()
screen.onkey(key="w", fun=L_paddle.move_up)
screen.onkey(key="s", fun=L_paddle.move_down)
screen.onkey(key="Up", fun=R_paddle.move_up)
screen.onkey(key="Down", fun=R_paddle.move_down)


game_state = True
while game_state:
    sleep(0.1)
    screen.update()
    ball.move()
    # print(f"{ball.y_direction}-{ball.x_direction} at {ball.xcor()},{ball.ycor()}")

screen.exitonclick()
