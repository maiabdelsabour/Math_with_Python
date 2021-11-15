"""
write a function called starSpiral()that will draw a spiral of stars
"""
from turtle import *

def starSpiral(sidelength):
    for i in range(5):
        forward(sidelength)
        right(144)

size = 20
for i in range(60):
    starSpiral(size)
    size = size + 5
    forward(10)
    right(5)




        