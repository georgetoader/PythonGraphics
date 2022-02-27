import turtle

def tree(plist, l, a, f, lev = 5):
    if l > 5:
        lst = []
        for p in plist:
            if lev > 0:
                p.pensize(lev)
            else:
                p.pensize(1)
            p.forward(l)
            q = p.clone()

            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)

        tree(lst, l * f, a, f, lev * 0.75)

def draw():
    p = turtle.Turtle()
    p.color("green")

    p.hideturtle()
    p.speed(0)
    p.left(90)
    p.goto(0, -270)
    p.pendown()

    tree([p], 270, 65, 0.6375, 20)

if __name__ == "__main__":
    draw()
    turtle.mainloop()