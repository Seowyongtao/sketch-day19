from turtle import Turtle, Screen

tim = Turtle()
myScreen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def move_clockwise():
    tim.right(10)


def move_anti_clockwise():
    tim.left(10)


def clear():
    tim.reset()


myScreen.listen()
myScreen.onkeypress(key="w", fun=move_forward)
myScreen.onkeypress(key="s", fun=move_backward)
myScreen.onkeypress(key="d", fun=move_clockwise)
myScreen.onkeypress(key="a", fun=move_anti_clockwise)
myScreen.onkeypress(key="c", fun=clear)
myScreen.exitonclick()
