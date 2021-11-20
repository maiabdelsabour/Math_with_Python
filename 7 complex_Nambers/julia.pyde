#range of x­values
xmin =-0.25 #xmin = -2 
xmax = 0.25 #xmax = 2
#range of y­values
ymin = -2 #ymin =-1
ymax = 2 #ymax =-0.5

#calculate the range
rangex = xmax-xmin
rangey = ymax-ymin
def setup():
    global xscl, yscl
    size(600,600)
    colorMode(HSB)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height
def draw():
    #origin in center:
    translate(width/2,height/2)
    #go over all x's and y's on the grid
    x = xmin
    while x < xmax:
    y = ymin
    while y < ymax:
        z = [x,y]
        c = [­0.8,0.156]
        #put it into the julia program
        col = julia(z,c,100)
        #if julia returns 100
        if col == 100:
            fill(0)
        else:
            #map the color from 0 to 100
             #to 0 to 255
             #coll = map(col,0,100,0,300)
             fill(3*col,255,255)
        rect(x*xscl,y*yscl,1,1)
        y += 0.01
    x += 0.01






from math import sqrt

def complexAdd(a,b):
    '''Adds two complex numbers'''
    return [a[0]+b[0],a[1]+b[1]]

def complexMultiply(a,b):
    '''
    (a+bi)(c+di)
    = ac + adi + bci + bdi**2
    = ac + (ad + bc)i + bd(-1)
    = ac - bd + (ad + bc)i
    = [ac-bd, ad+bd]
    '''
    return [a[0]*b[0]-a[1]*b[1],a[1]*b[0]+a[0]*b[1]]

def magnitude(a):
    # Pythagorean theorem
    return sqrt(a[0]**2 + a[1]**2)

def cAdd(a,b):
    '''adds two complex numbers'''
    return [a[0]+b[0],a[1]+b[1]]
def cMult(u,v):
    '''Returns the product of two complex numbers'''
    return[u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]
def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)
def mandelbrot(z,num):
    '''runs the process num times
    and returns the diverge count '''
    count=0
    #define z1 as z
    z1=z
    #iterate num times
    while count <= num:
        #check for divergence
        if magnitude(z1) > 2.0:
        #return the step it diverged on
            return count
        #iterate z
        z1=cAdd(cMult(z1,z1),z)
        count+=1
    #if z hasn't diverged by the end
    return num
def julia(z,c,num):
    '''runs the processs num times and returns the diverge count'''
    count=0
    #define z1 as z 
    z1 = z 
    #iterate num times
    while count<= num:
        #check for divergence
        if magnitude(z1)>2.0:
            #return the step it divered on
            return count
        #iterate z
        z1 = cAdd(cMult(z1,z1),c)
        count+=1


