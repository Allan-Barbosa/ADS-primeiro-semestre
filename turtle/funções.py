import turtle
turtle.Screen()
turtle.shape('turtle')


def quadrado(lado):
    for i in range(4):
        turtle.fd(lado)
        turtle.lt(90)


def retangulo(largura, altura):
    for i in range(2):
        turtle.fd(largura)
        turtle.lt(90)
        turtle.fd(altura)
        turtle.lt(90)


def triangulo(lado):
    for i in range(3):
        turtle.fd(lado)
        turtle.lt(120)


triangulo(150)
