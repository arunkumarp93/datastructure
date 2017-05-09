import turtle
def tree(branchlen,t):
    if branchlen > 5:
        t.forward(branchlen)
        t.right(20)
        tree(branchlen-15,t)
        t.left(40)
        t.pensize(1.5)
        tree(branchlen-15,t)
        t.right(20)
        t.backward(branchlen)
def main():
    t = turtle.Turtle()
    mywin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    """
    pensize changed for the width

    """
    t.pensize(5)
    t.color("black")
    tree(75,t)
    mywin.exitonclick()

main()
