"""
EXERCISE 1­4: POLYGON FUNCTIONS
Write a function called polygonthat takes an integer as an argument and
makes the turtle draw a polygon with that integer’s number of sides.
"""

from turtle import *

def polygon(sidelength=100):
    for i in range(6):
        forward(sidelength)
        right(60)

polygon()
