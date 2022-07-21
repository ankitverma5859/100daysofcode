import random
import turtle
import turtle as t
import random
import colorgram

colours = ["lime green", "dark red", "medium violet red", "sandy brown", "dark violet", "blue", "yellow", "green",
           "purple", "orange"]
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed("fast")

# Draw a rectangle
'''
for _ in range(4):
    tim.forward(100)
    tim.left(90)
'''

# Draw a dashed line
'''
for _ in range(10):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5)
'''

#Draw the shapes
'''
def draw(sides, length, color):

    for _ in range(sides):
        angle = 360 / sides
        tim.color(color)
        tim.forward(length)
        tim.right(angle)


start_length = 100
for i in range(3, 11):
    draw(i, start_length, random.choice(colours))
'''

# Random Walk
'''
tim.pensize(15)
tim.speed("fastest")


def random_walk():
    for _ in range(100):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))


random_walk()
'''

# Spirograph Effect

'''
def draw_spirograph(circle_gap):
    for _ in range(int(360 / circle_gap)):
        tim.color(random_color())
        tim.speed("fastest")
        tim.circle(100)
        tim.setheading(tim.heading() + circle_gap)


draw_spirograph(5)
'''

# Spot Painting
colors = colorgram.extract('spot_painting.png', 10)
rgb_colors = []
for color in colors:
    rgb_colors.append(color.rgb)

num_of_dots = 100;

tim.penup()
tim.hideturtle()
tim.setheading(255)
tim.forward(200)
tim.setheading(0)

for dots in range(1, num_of_dots):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)

        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
