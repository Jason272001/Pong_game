from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player1=0
        self.player2=0
        self.color("white")
        self.penup()
        self.goto(0,300)
        self.write(f"{self.player1} | {self.player2}",align="center", font=("Arial",35,"normal"))
        self.hideturtle()

    def update(self):
        self.write(f"{self.player1} | {self.player2}", align="center", font=("Arial", 35, "normal"))

    def increase(self,player):
        if player == 1:
            self.player1+=1
        elif player ==2:
            self.player2+=1
        self.clear()
        self.update()