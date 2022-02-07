from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.update_score()


