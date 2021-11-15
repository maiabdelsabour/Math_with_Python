
"""
EXERCISE 1­3: TRI AND TRI AGAIN
Write atriangle()function that will draw a triangle of a given “side length.”
"""
from turtle import *

def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(240)

    forward(sidelength)
    forward(sidelength)

triangle()
