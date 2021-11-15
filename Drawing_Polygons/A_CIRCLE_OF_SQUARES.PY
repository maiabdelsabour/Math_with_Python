"""
EXERCISE 1­2: A CIRCLE OF SQUARES
Write and run a function that draws 60 squares, turning right 5 degrees after
each square. Use a loop! Your result should end up looking like this:

"""
from turtle import *

def circle_of_squares(sidelength=100):
    for i in range(4):
            forward(sidelength)
            right(90)

circle_of_squares(50)
circle_of_squares(30)
circle_of_squares()






