import turtle
import random

screen = turtle.Screen()
screen.colormode(255)

timmy = turtle.Turtle()
timmy.speed("fastest")
timmy.penup()

random_color = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177)]


for k in range(-300, 301, 60):
    for i in range(-300, 301, 60):
        timmy.setpos(i, k)
        timmy.dot(20, random.choice(random_color))

# timmy.setpos(300, 300)
# timmy.dot(20, random_color[3])
# timmy.setpos(240, 300)
# timmy.dot(20, random_color[4])
# timmy.setpos(-300, -300)
# timmy.dot(20, random_color[6])

# def new_color():
#     random_color = []
#     for _ in range(3):
#         random_color.append(random.randint(0, 255))
#     return timmy.pencolor(random_color[0], random_color[1], random_color[2])

# for i in range(3, 361, 3):
#     new_color()
#     timmy.circle(50)
#     timmy.setheading(i)

# for _ in range(200):
#     new_color()
#     timmy.setheading(random_walk())
#     timmy.forward(30)
    # timmy.setheading(random.choice(directions))

screen.exitonclick()
