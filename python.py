import turtle

turtle.Screen().bgcolor("aqua")
board = turtle.Turtle()

#first triangle for star
board.forward(100)  #draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

#second triangle for star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()


import turtle  #importing turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(700,800)
polygon = turtle.Turtle()  #defined variable

num_sides = 400  #variable
side_lengh = 2
angle = 360.0 / num_sides
#iterate loop for total number of sides
for i in range(num_sides):
    polygon.forward(side_lengh)
    polygon.right(angle)

turtle.done()