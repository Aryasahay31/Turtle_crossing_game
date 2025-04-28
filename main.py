from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

my_screen = Screen()
my_screen.listen()
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

my_screen.onkey(fun=player.move, key= "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    my_screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #Detect collision with the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()
    #Detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()






my_screen.exitonclick()
