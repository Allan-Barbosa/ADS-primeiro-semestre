import turtle
turtle.Screen()
turtle.bgcolor("lightgreen")
turtle.shape('turtle')
turtle.color('blue')
turtle.penup()
for i in range(5, 120, 2):
    turtle.stamp()
    turtle.fd(i)
    turtle.right(24)
