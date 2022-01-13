import turtle
import random

screen = turtle.Screen()
screen.colormode(255)

timmy = turtle.Turtle()
timmy.pensize(1)
timmy.shape("turtle")
timmy.speed("fastest")


def new_color():
    random_color = []
    for _ in range(3):
        random_color.append(random.randint(0, 255))
    return timmy.pencolor(random_color[0], random_color[1], random_color[2])


for i in range(3, 361, 3):
    new_color()
    timmy.circle(50)
    timmy.setheading(i)
# for _ in range(200):
#     new_color()
#     timmy.setheading(random_walk())
#     timmy.forward(30)
    # timmy.setheading(random.choice(directions))

screen.exitonclick()
