from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.current_speed = 0.1
        self.width = 20
        self.speed(self.current_speed)
        self.x_step = 10
        self.y_step = 10

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce(self, wall):
        if wall:
            self.y_step *= -1
        else:
            self.x_step *= -1
            self.current_speed *= 0.9
