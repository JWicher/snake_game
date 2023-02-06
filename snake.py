from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.starting_positions = [(-20, 0), (-40, 0), (-60, 0)]
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.snake_segments.append(segment)

    def increse_snake_size(self):
        last_segment = self.snake_segments[-1]
        new_position = (last_segment.xcor(), last_segment.ycor())
        self.add_segment(new_position)

    def move(self):
        for segment_num in range(len(self.snake_segments) - 1, 0, -1):
            x = self.snake_segments[segment_num - 1].xcor()
            y = self.snake_segments[segment_num - 1].ycor()
            self.snake_segments[segment_num].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



