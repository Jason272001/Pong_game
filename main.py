
from turtle import Screen
from player import Player
from ball import Ball
from score import Score
import time
screen=Screen()
screen.setup(width=1200,height=700)

screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
score=Score()
player1=Player(-550)
player2=Player(550)
ball=Ball()

keys_pressed={"w":False,"s":False,"Up":False,"Down":False}

def key_down_w():
        keys_pressed["w"]=True
        move_player1_up()

def key_up_w():
        keys_pressed["w"]=False


def key_down_s():
        keys_pressed["s"] = True
        move_player1_down()


def key_up_s():
        keys_pressed["s"] = False

def key_down_up():
    keys_pressed["Up"] = True
    move_player2_up()

def key_up_up():
    keys_pressed["Up"] = False

def key_down_down():
    keys_pressed["Down"] = True
    move_player2_down()

def key_up_down():
    keys_pressed["Down"] = False



def move_player1_up():
        if keys_pressed["w"] and player1.ycor()<300:
                player1.up()
                screen.ontimer(move_player1_up,15)

def move_player1_down():
        if keys_pressed["s"] and player1.ycor()>-300:
                player1.down()
                screen.ontimer(move_player1_down,15)

def move_player2_up():
    if keys_pressed["Up"]and player2.ycor()<300:
        player2.up()
        screen.ontimer(move_player2_up, 15)

def move_player2_down():
    if keys_pressed["Down"] and player2.ycor()>-300:
        player2.down()
        screen.ontimer(move_player2_down, 15)

screen.listen()


screen.onkeypress(key_down_w,"w")
screen.onkeyrelease(key_up_w, "w")

screen.onkeypress(key_down_s, "s")
screen.onkeyrelease(key_up_s, "s")

screen.onkeypress(key_down_up, "Up")
screen.onkeyrelease(key_up_up, "Up")

screen.onkeypress(key_down_down, "Down")
screen.onkeyrelease(key_up_down, "Down")



game_is_on=True

while game_is_on:
        time.sleep(ball.ball_speed)
        screen.update()
        ball.move()





        if ball.ycor() > 330 or ball.ycor() < -330:
                ball.bounce_y()


        if ball.distance(player2) < 50 and ball.xcor() > 520 or ball.distance(player1) < 50 and ball.xcor() < -530:
                 ball.bounce_x()


        if ball.xcor()>560 :
                score.increase(1)
                ball.reset()

        if ball.xcor() < -560:
                score.increase(2)
                ball.reset()



screen.exitonclick()