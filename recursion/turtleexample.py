import turtle

myturtle=turtle.Turtle()
mywin=turtle.Screen()

def firstturtle(myturtle,linelen):
    if linelen > 0:
        myturtle.forward(linelen)
        myturtle.right(90)
        firstturtle(myturtle,linelen-10)
firstturtle(myturtle,100)
mywin.exitonclick()
