def setup():
    size(600,600)
    noFill()
    
# def draw():
#     beginShape()
#     vertex(100,100)
#     vertex(100,200)
#     vertex(200,200)
#     vertex(200,100)
#     vertex(150,50)
#     endShape(CLOSE)

# def draw():
#     translate(width/2,height/2)
#     beginShape()
#     for i in range(6):
#         vertex(100*cos(radians(60*i)),100*sin(radians(60*i)))
#     endShape(CLOSE)

def draw():
    translate(width/2,height/2)
    polygon(3,100)#3 sides, vertices 100 units from the center
def polygon(sides,sz):
    # draws a polygon given the number of sides and from th center
    beginShape()
    for i in range(sides):
        step = radians(360/sides)
        vertex(sz*cos(i*step),sz*sin(i*step))
    endShape(CLOSE)