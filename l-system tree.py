import turtle
import random
# Дерево сделал сам, только l систему нашел в инете
axiom = "X"
rules = {"X": "F[@[-X]+X]", "F": "F", "[": "[", "+": "+", "@": "@", "-": "-", "]": "]"}
generation = 13
created_gen = ""


def line_generator(lst, new_gen, current_gen=0):
    new_gen_line = ""
    for i in lst:
        if i in rules:
            new_gen_line += rules[i]
    current_gen += 1
    if new_gen == current_gen:
        return new_gen_line
    return line_generator(new_gen_line, new_gen, current_gen)


total_lst = line_generator(axiom, generation)
memory_lst = []
pen_thickness = 15
brunch_length = 110
g = 0.250
screen = turtle.Screen()
turtle.screensize(canvwidth=4000, canvheight=4000,
                  bg="black")
turtle.tracer(0, 0)
turtle.hideturtle()
turtle.penup()
turtle.rt(90)
turtle.fd(1000)
turtle.lt(180)
turtle.pendown()
turtle.pencolor(0.1, 0.1, 0.1)
for i in total_lst:
    if i == "X":
        turtle.pensize(pen_thickness)
        turtle.fd(brunch_length)
    if i == "F":
        turtle.pensize(pen_thickness)
        turtle.fd(brunch_length)
    if i == "+":
        turtle.rt(random.randint(0, 45))
    if i == "-":
        turtle.lt(random.randint(0, 45))
    if i == "[":
        memory_lst.append([turtle.pos(), turtle.heading(), pen_thickness, brunch_length, turtle.pencolor()])
    if i == "]":
        current_position = memory_lst.pop()
        turtle.setpos(current_position[0])
        turtle.seth(current_position[1])
        pen_thickness = current_position[2]
        brunch_length = current_position[3]
        turtle.pencolor(current_position[4])
    if i == "@":
        pen_thickness *= random.uniform(0.8, 0.9)
        brunch_length *= random.uniform(0.8, 0.9)
        g += 0.099
        if g <= 1:
            turtle.pencolor(g, g, g)

turtle.done()
