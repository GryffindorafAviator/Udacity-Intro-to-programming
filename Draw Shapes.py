import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)
    for i in range(4):
        brad.forward(100)
        brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("green")
    for i in range(3):
        bob.backward(100)
        bob.left(120)
        bob.speed(1)

    window.exitonclick()

draw_shapes()
