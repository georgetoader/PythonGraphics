import turtle
import random

def polygon(pen, l, n) :
    angle = 360.0 / n
    for i in range(n) :
        pen.forward(l)
        pen.right(angle)

def star(pen, l, n=5) :
    for i in range(n) :
        pen.forward(l)
        pen.right(144)

def draw():
    bob=turtle.Turtle()
    turtle.tracer(0)
    turtle.bgcolor("black")

    for y in range(15):
        xpos=random.randint(-100,100)
        ypos=random.randint(-100,100)

        col1=random.random()%256
        col2=random.random()%256
        col3=random.random()%256
        col=(col1,col2,col3)

        bob.penup()
        bob.goto(xpos,ypos)
        bob.pendown()

        for times in range(2000):
            star(bob, 150)
            bob.left(15)
            bob.color(col)
            bob.pensize(0)
            bob.left(15)

        polygon(bob, 20,  6)

if __name__ == "__main__":
    draw()
    turtle.mainloop()