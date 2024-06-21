import colorgram
import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()


def extract_colors():
    hirst_colors = colorgram.extract("image.jpg", 100)
    colors_list = []
    for image in hirst_colors:
        colors_list.append((image.rgb.r, image.rgb.g, image.rgb.b))
    return colors_list


def make_painting():
    y_position = -250.00
    for _ in range(10):
        tim.goto(x=-250.00, y=y_position)
        for i in range(10):
            tim.dot(20, random.choice(extract_colors()))
            tim.forward(50)
        y_position += 50


make_painting()
my_screen = turtle.Screen()
my_screen.exitonclick()
