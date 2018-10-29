# Example 2
# Write code to draw the staircase
# pattern above.  The modulo operation
# might be useful!

import turtle


def stair(tur):
    for _ in range(8):
        tur.forward(50)
        if _ % 2:
            tur.right(90)
        else:
            tur.left(90)


t = turtle.Turtle()
t.penup()
t.back(200)
t.pendown()
t.width(2)
t.color("yellow")
t.hideturtle()

stair(t)


