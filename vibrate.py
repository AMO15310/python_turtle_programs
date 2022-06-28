import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.pensize(1)
t.speed(0)
turtle.title("Vibrate circle")
s.bgcolor('black')
t.pencolor("red")
a = 0
b = 0
while(True):
    t.fd(a)
    t.rt(b)
    a+=1
    b+=1
    if b==210: 
        break
turtle.mainloop()