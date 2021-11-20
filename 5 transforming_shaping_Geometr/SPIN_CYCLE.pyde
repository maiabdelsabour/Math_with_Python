"""
EXERCISE 5­1: SPIN CYCLE
Create a circle of equilateral triangles in a Processing sketch and rotate them
using the rotate()function.
"""

def setup():
    size(600,600)
t=0
def setup():
    size(600,600)
def draw():
    global t
    #set background white
    background(225)
    translate(width/2,height/2);
    rotate(radians(t))
    for i in range(12):
        triangle(200,0, 260,0, 230, 40)
        rotate(radians(360/12))
    t+=1
