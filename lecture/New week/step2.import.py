# from RSP_Game import getstartRSPgame
#
# getstartRSPgame(4)


# from typing_game import getstarwordgame
#
# getstarwordgame(1)

# 모듈함수

import turtle
t = turtle.Turtle()

def square(len):
    for i in range (4):
        t.forward(len)
        t.left(90)
        turtle.pensize(5)


def triangle(len):
    for i in range (10):
        t.forward(len)
        t.right(45)

def circle(len):
    for i in range (5):

len = 50
while 70> len :
    square(len)
    len += 100
    triangle(len)
    len += 400
