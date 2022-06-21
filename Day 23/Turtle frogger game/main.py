import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

# Move Turlte up
screen.listen()
screen.onkeypress(player.player_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Reset the turtle to start after reaching finish
    if player.ycor() > 280:
        player.return_to_start()
        scoreboard.level_up()
        car_manager.level_up()

    # Detect player collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False


screen.exitonclick()
