import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet",prompt="which turtle will win the race.")
colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
y_position = [-70,-40,-10,20,50,80]
all_turtle = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    if turtle.xcor() > 230:
        is_race_on = False
        wining_color = turtle.pencolor()
        if wining_color == user_bet:
            print(f"you have won the race! The color {wining_color} turtle is winner!")
        else:
            print(f"you have lost the race! The color {wining_color} turtle is winner!")
    for turtle in all_turtle:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()