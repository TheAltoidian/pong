from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.y_direction = "up"
        self.x_direction = "right"
        self.variable_speed = 10

    def up_right(self):
        if self.ycor() < 300:
            if self.xcor() < 540:
                new_x = self.xcor() + self.variable_speed
                new_y = self.ycor() + self.variable_speed
                self.teleport(new_x, new_y)
            else:
                self.x_direction = "left"
        else:
            self.y_direction = "down"

    def down_right(self):
        if self.ycor() > -290:
            if self.xcor() < 540:
                new_x = self.xcor() + self.variable_speed
                new_y = self.ycor() - self.variable_speed
                self.teleport(new_x, new_y)
            else:
                self.x_direction = "left"
        else:
            self.y_direction = "up"

    def up_left(self):
        if self.ycor() < 300:
            if self.xcor() > -540:
                new_x = self.xcor() - self.variable_speed
                new_y = self.ycor() + self.variable_speed
                self.teleport(new_x, new_y)
            else:
                self.x_direction = "right"
        else:
            self.y_direction = "down"

    def down_left(self):
        if self.ycor() > -300:
            if self.xcor() > -540:
                new_x = self.xcor() - self.variable_speed
                new_y = self.ycor() - self.variable_speed
                self.teleport(new_x, new_y)
            else:
                self.x_direction = "right"
        else:
            self.y_direction = "up"

    def move(self):
        if self.y_direction == "up":
            if self.x_direction == "right":
                self.up_right()
            else:
                self.up_left()
        else:
            if self.x_direction == "right":
                self.down_right()
            else:
                self.down_left()
