t = 0
points = []
def setup():
    size(600,600)
    noStroke()
    
    
# def draw():
#     global t,points
#     a1,a2 = 100,200 #amplitudes
#     f1,f2 = 1,2 #frequencies
#     p1,p2 = 0,PI/2 #phase shifts
#     d1,d2 = 0.02,0.02 #decay constants
#     background(255)
#     translate(width/2,height/2)
#     x = a1*cos(f1*t + p1)*exp(-d1*t)
#     y = a2*cos(f2*t + p2)*exp(-d2*t)
#     # fill(0)#black
#     # ellipse(x,y,5,5)

#     #save location to points list
#     points.append([x,y])
#     #go through points list and draw lines between them
#     for i,p in enumerate(points):
#         stroke(0)#black
#         if i<len(points)-1:
#             line(p[0],p[1],points[i+1][0],points[i+1][1])
#     t+=.1




def draw():
    background(255)
    translate(width/2,height/2)
    points = []
    t = 0
    while t < 1000:
        points.append(harmonograph(t))
        t += 0.01
    #go through points list and draw lines between them
    for i,p in enumerate(points):
        stroke(255,0,0) #red
        if i<len(points)-1:
            line(p[0],p[1],points[i+1][0],points[i+1][1])
    
def harmonograph(t):
    a1=a2=a3=a4 = 100
    f1,f2,f3,f4 = 2.01,3,3,2
    p1,p2,p3,p4 = -PI/2,0,-PI/16,0
    d1,d2,d3,d4 = 0.00085,0.0065,0,0
    x = a1*cos(f1*t + p1)*exp(-d1*t) + a3*cos(f3*t + p3)*exp(-d3*t)
    y = a2*sin(f2*t + p2)*exp(-d2*t) + a4*cos(f4*t + p4)*exp(-d4*t)
    return [x,y]



    