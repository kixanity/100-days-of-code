import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()
screen.listen()


def fw():
    timmy.forward(50)


def bw():
    timmy.backward(50)


def lt():
    timmy.left(3)


def rt():
    timmy.right(3)


screen.onkey(fw, "w")
screen.onkey(bw, "s")
screen.onkey(lt, "a")
screen.onkey(rt, "d")

screen.exitonclick()
