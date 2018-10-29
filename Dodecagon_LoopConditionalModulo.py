import turtle

# Example 3
t = turtle.Turtle()
t.width(5)

for n in range(12):
    t.color("gray")
    # Add some if statements (with modulo) here!
    if n % 3 == 0:
        t.color("red")
    elif n % 3 == 1:
        t.color("orange")
    else:
        t.color("yellow")
    t.forward(50)
    t.right(360/12)
