import turtle
turtle.Screen()
turtle.shape('turtle')
def poligono(lado,numero_de_lados):
    for i in range(numero_de_lados):
        turtle.fd(lado)
        turtle.lt(360/numero_de_lados)
poligono(100,3)
