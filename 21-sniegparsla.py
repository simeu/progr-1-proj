#!/bin/python3

import turtle
import random
pp = turtle.Turtle()
turtle.Screen().bgcolor("black")
colours = ["magenta", "cyan"]
pp.color("magenta")
for i in range(10):
    for i in range(2):
        pp.forward(100)
        pp.right(60)
        pp.forward(100)
        pp.right(120)
    pp.right(36)
    pp.color(random.choice(colours))
