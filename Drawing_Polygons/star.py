"""
write a “star” function that will draw a five­pointed star
"""
from turtle import *

def star(sidelength=100):
    for i in range(5):
        forward(sidelength)
        right(144)

star()