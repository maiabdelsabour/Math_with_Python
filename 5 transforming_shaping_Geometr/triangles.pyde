def setup():
    size(600, 600)
    rectMode(CENTER)

t=0
def draw():
    global t 
    translate(width/2,height/2)
    rotate(radians(t))
    triangle(0,0,100,100,200,-200)
    t+=0.5



t=0
def draw():
    global t
    translate(width/2,height/2)
    rotate(radians(t))
    tri(200) #draw the equilateral triangle
    t += 0.5
def tri(length):
    '''Draws an equilateral triangle around center of triangle'''
    triangle(0,-length,-length*sqrt(3)/2, length/2, length*sqrt(3)/2, length/2)
  


t = 0
def draw():
    global t
    background(255)#white
    translate(width/2,height/2)
    for i in range(90):
        #space the triangle evenly around the circle
        rotate(radians(360/90))
        pushMatrix()#save this orientation
        #go to circumference of circle
        translate(200,0)
        #spin each triangle 
        # rotate(radians(t))
        # rotate(radians(t+i))
        # rotate(radians(t+i*360/90))
        rotate(radians(t+2*i*360/90))
        #draw the triangle
        tri(100)
        popMatrix()
    t+=0.5
def tri(length):
    noFill()#makes the triangle transparent
    triangle(0,-length,-length*sqrt(3)/2,length/2,length*sqrt(3)/2,length/2)
    