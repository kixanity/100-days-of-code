from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_x = random.randint(-300, 300)
        new_y = random.randint(-300, 300)
        self.goto(new_x, new_y)
