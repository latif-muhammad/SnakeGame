from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.7, 0.7)
        self.penup()
        self.color('yellow')
        self.speed("fastest")
        self.newFood()

    def newFood(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

