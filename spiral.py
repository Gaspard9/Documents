import turtle  #importing library
my_wn = turtle.Screen()
my_wn.bgcolor("red")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0
while True:  #iterate loop
    for i in range(4):
        my_pen.fd(size + 5)
        my_pen.left(1)
        size = size - 5
    size = size + 1