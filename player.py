from turtle import Turtle

class Player(Turtle):
        def __init__(self,position):
            self.position=position
            super().__init__()
            self.create_player(self.position)

        def create_player(self,position):
            # Assign the Turtle instance to self.body
            self.shape("square")
            self.color("white")
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.penup()
            self.goto(position, 0)

        def up(self):
            new_Y = self.ycor() + 15
            self.goto(self.xcor(), new_Y)

        def down(self):
            new_Y = self.ycor() - 15
            self.goto(self.xcor(), new_Y)