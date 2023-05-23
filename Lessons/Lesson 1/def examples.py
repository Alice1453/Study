import turtle

def move(a):
    turtle.forward(a)
    turtle.left(90)

def draw_square(a):
    for i in range(4):
        move(a)

def draw_square_color(a, color):
    turtle.color(color)
    turtle.begin_fill()
    draw_square(a)
    turtle.end_fill()

turtle.speed(1)

draw_square_color(75, "red")
turtle.goto(150, 150)
draw_square_color(100, "green")