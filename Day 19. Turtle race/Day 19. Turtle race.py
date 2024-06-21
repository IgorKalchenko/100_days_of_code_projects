from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
color_str = ", ".join(color for color in colors)
user_bet = screen.textinput(
    title="Make your bet",
    prompt=f"Which turtle will win the race? Enter a color ({color_str}): ")
all_turtles = []

x_coordinate = -240
y_coordinate = -150

for color in colors:
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.color(color)
    my_turtle.goto(x=x_coordinate, y=y_coordinate)
    y_coordinate += 50
    all_turtles.append(my_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
