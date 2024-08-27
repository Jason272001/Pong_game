from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.ball_speed= 0.07

    def move(self):
        new_X=self.xcor()+self.x_move
        new_Y=self.ycor()+self.y_move
        self.goto(new_X,new_Y)

    def bounce_y(self):
        self.y_move *=-1

    def bounce_x(self):
            self.x_move *= -1
            self.ball_speed*=0.5

    def reset(self):
        self.goto(0,0)
        self.ball_speed=0.07
        self.bounce_x()