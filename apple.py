from turtle import Turtle
import random

class Apple(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('red')
        self.penup()
        self.set_new_position()

    def set_new_position(self):
        random_pos_x = random.randint(-280, 280)
        random_pos_y = random.randint(-280, 280)
        self.setposition(random_pos_x, random_pos_y)
