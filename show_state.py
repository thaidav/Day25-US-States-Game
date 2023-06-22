from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 10, "normal")

class ShowState(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.speed("fastest")
        self.hideturtle()

    def update_state(self, answer, x_cor, y_cor):
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(f"{answer}", align=ALIGN, font=FONT)
        self.pendown()
