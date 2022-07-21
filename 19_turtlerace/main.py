from turtle import Turtle, Screen
import random

#tim = Turtle()
screen = Screen()

'''
def move_up():
    tim.forward(10)


def move_down():
    tim.backward(10)


def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
#screen.onkey(key="space", fun=move_forward)
screen.onkey(key="d", fun=move_left)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="c", fun=clear)
'''

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet.", prompt="Which turtle will win the race? Enter a color: ")

colours = ["violet", "indigo", "blue", "green", "yellow", "orange"]
y_coords = [120, 80, 40, 0, -40, -80]
is_race_on = False
turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(-230, y_coords[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print("Your Win!")
            else:
                print('You Loose!')
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()