import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.shape("turtle")

# count = 0
# while count != 4:
for _ in range(6):
    timmy.forward(100)
    timmy.right(90)
    # count += 1

screen.exitonclick()
