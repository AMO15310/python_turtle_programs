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
curve(200)
turtle.mainloop()