import turtle
turtle.Screen()
turtle.shape('turtle')
def quadrado(lado,color):
    c=0
    for y in range(5):
        for x in range(4):
            turtle.pd()
            turtle.color(color)
            turtle.fd(lado)
            turtle.lt(90)
        turtle.up()
        turtle.rt(140)
        turtle.fd(20)
        turtle.lt(140)
        lado+=30
        color='green'
        c+=1
        if c==2:
            color='blue'
        if c==3:
            color='black'
        if c==4:
            color='yellow'
quadrado(100,'red')
