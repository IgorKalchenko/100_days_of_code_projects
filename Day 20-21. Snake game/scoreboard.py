from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = -1
        self.penup()
        self.speed("fastest")
        self.goto(0, 280)
        self.color("white")
        self.draw_score()

    def draw_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
