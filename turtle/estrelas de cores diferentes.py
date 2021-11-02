import turtle
from turtle import*
Screen().bgcolor('black')
shape('turtle')
speed(10)


def estrela(lado, cor):
    pd()
    color(cor)
    begin_fill()
    for i in range(5):
        fd(lado)
        lt(144)
    end_fill()
    up()
    lt(90)
    fd(200)


estrela(100, 'white')
estrela(80, 'red')
estrela(120, 'yellow')
ht()
