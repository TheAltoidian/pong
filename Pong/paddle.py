from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.shape("square")
        self.shapesize(stretch_wid=3.5, stretch_len=1)
        self.color("white")
        self.speed("fastest")

    def start_left(self):
        self.teleport(x=-560, y=0)
        self.showturtle()

    def start_right(self):
        self.teleport(x=560, y=0)
        self.showturtle()

    def move_up(self):
        if self.ycor() < 270:
            self.setheading(90)
            self.forward(30)
            self.setheading(0)

    def move_down(self):
        if self.ycor() > -270:
            self.setheading(270)
            self.forward(30)
            self.setheading(0)