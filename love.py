import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.color("red","pink")

def curve(x):
    for i in range(x):
        t.rt(1)
        t.fd(1)
t.begin_fill()
t.lt(140)
t.fd(111.65)
curve(200)
t.lt(120)
curve(200)
t.fd(111.65)
t.end_fill()
turtle.mainloop()