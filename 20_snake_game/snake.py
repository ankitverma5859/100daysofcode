from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(position)
        self.snake_segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for segment_num in range(len(self.snake_segments) - 1, 0, -1):
            x_new = self.snake_segments[segment_num - 1].xcor()
            y_new = self.snake_segments[segment_num - 1].ycor()
            self.snake_segments[segment_num].goto(x_new, y_new)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)

    def down(self):
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(DOWN)

    def right(self):
        if self.snake_segments[0].heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)

    def left(self):
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)