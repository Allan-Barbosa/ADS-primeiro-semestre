import turtle
from turtle import*
Screen().bgcolor('black')
shape('turtle')
color('white')
speed(10)


def estrela(lado):
    begin_fill()
    for i in range(5):
        fd(lado)
        lt(144)
    end_fill()
    up()
    fd(200)
    ht()


done()
estrela(100)
