from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.go_to_start()

    def is_finished(self):
        return self.ycor() == FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_forward(self):
        if not self.is_finished():
            self.goto(x=self.xcor(), y=self.ycor() + MOVE_DISTANCE)
        else:
            self.goto(STARTING_POSITION)