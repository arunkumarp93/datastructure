"""
Draw triangle inside the triangle
"""
import turtle
def drawtriangle(points,turtle):
    """
    TO draw the triangle perfectly used the
    from down to up below lines used

    either below line not give turtle start from the goto line

    and draw traindgle which don't look like triangle

    it go upward 0 to 100

    """

    turtle.up()
    turtle.goto(points[0][0],points[0][1])
    turtle.down()

    """
    draw triangle

    first line points[1][0] is 100 and [1][1] is 0 so
    line move 100 to 0 down because turtle.down()

    second line -100 to 0 move the line upto -100.

    third line move 0 to 100 which connect to the top of the
    triangle

    """

    turtle.goto(points[1][0],points[1][1])

    turtle.goto(points[2][0],points[2][1])

    turtle.goto(points[0][0],points[0][1])

def getmid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def sierpinski(points,degree,turtle):
    drawtriangle(points,turtle)
    if degree > 0:
        """
        Draw inner triangle
        
        """
        sierpinski([points[0],
                    getmid(points[0],points[1]),
                    getmid(points[0],points[2])],
                   degree-1,turtle)

        sierpinski([points[1],
                    getmid(points[0],points[1]),
                    getmid(points[1],points[2])
                    ],degree-1,turtle)

        sierpinski([points[2],
                     getmid(points[2],points[0]),
                     getmid(points[2],points[1])
                    ],degree-1,turtle)
def main():
    t =turtle.Turtle()
    mywin=turtle.Screen()
    points=[[0,100],[100,0],[-100,0]]
    sierpinski(points,3,t)
    mywin.exitonclick()
main()
