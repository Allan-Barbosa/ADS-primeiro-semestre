import turtle
import random
turtle.Screen()
turtle.shape('turtle')
turtle.bgcolor('black')
def posicao_aleatoria():
    turtle.penup()
    turtle.goto(random.randint(-400,400),random.randint(-400,400))
    turtle.pendown()
def estrela(lado):
    turtle.color('white')
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.fd(lado)
        turtle.lt(144)
    turtle.end_fill()
    turtle.up()
for x in range(30):
    posicao_aleatoria()
    estrela(random.randint(5,25))
turtle.ht()
turtle.done()
