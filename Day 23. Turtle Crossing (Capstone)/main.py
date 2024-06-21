import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


car_manag = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True
tortoise = Player()
scr = Scoreboard()
screen.listen()
screen.onkey(tortoise.move_forward, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manag.create_car()
    car_manag.move()
    scr.update_level()
    for car in car_manag.all_cars:
        if car.distance(tortoise) < 20:
            game_is_on = False
            scr.game_over()
    if tortoise.is_finished():
        car_manag.speed_up()
        tortoise.go_to_start()
        scr.increase_level()

screen.exitonclick()
