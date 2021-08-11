from turtle import Turtle

MOVE_DISTANCE: int = 20
POSITION = ((0, 0), (-20, 0), (-40, 0))
UP: int = 90
DOWN: int = 270
LEFT: int = 180
RIGHT: int = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]


    def create(self):
        for position in POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segments = Turtle("square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.create()
        self.head = self.segments[0]



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg_num - 1].xcor()
            y_pos = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_pos, y_pos)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
