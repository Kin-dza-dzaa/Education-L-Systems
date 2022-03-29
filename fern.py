import turtle
import random


screen = turtle.Screen()
screen.screensize(10000, 10000)
turtle.penup()
x = 0
y = 0
turtle.setpos(x, y)
turtle.dot(10, 'green')
turtle.speed(0)
turtle.hideturtle()
# turtle.tracer(0, 0)
for i in range(15000):
    random_number = random.choice([i for i in range(1, 101)])
    if random_number == 1:
        x = 0
        y *= 0.16
        turtle.setpos(100*x, 100*y)
        turtle.dot(2, 'green')
    elif random_number in [z for z in range(2, 87)]:
        x = 0.85*x + 0.04*y
        y = -0.04*x + 0.85*y + 1.6
        turtle.setpos(100*x, 100*y)
        turtle.dot(2, 'green')
    elif random_number in [k for k in range(87, 94)]:
        x = 0.2 * x - 0.26 * y
        y = 0.23 * x + 0.22 * y + 1.6
        turtle.setpos(100*x, 100*y)
        turtle.dot(2, 'green')
    elif random_number in [o for o in range(94, 101)]:
        x = -0.15 * x + 0.28 * y
        y = 0.26 * x + 0.24 * y + 0.44
        turtle.setpos(100*x, 100*y)
        turtle.dot(2, 'green')

turtle.done()
