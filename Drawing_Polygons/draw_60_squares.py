"""
EXERCISE 1­5: TURTLE SP IRAL
Make a function to draw 60 squares, turning 5 degrees after each square
and making each successive square bigger. Start at a lengthof 5 and
increment 5 units every square. It should look like this:
"""
from turtle import * 

def draw_multicolor_square(sidelength=1000):
    """Make turtle t draw a multi-color square of sz."""
    for i in range(4):
        forward(sidelength)
        right(90)

size = 20             # Size of the smallest square
for i in range(60):
    draw_multicolor_square(size)
    size = size + 5        # Increase the size for next time
    forward(10)        # Move tess along a little
    right(5)          #    and give her some turn

