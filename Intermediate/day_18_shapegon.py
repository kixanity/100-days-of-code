import turtle
import random

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.shape("turtle")
timmy.pensize(4)
screen.colormode(255)


def new_color():
    random_color = []
    for _ in range(3):
        random_color.append(random.randint(0, 255))
    # for i in range(3, 6):
    return timmy.pencolor(random_color[0], random_color[1], random_color[2])


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        timmy.forward(100)
        timmy.right(angle)

# print(random_color)


for gon in range(3, 11):
    new_color()
    draw_shape(gon)

screen.exitonclick()
