
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

def mandelbrot(a,num):
    # runs the process num times and returns the diverge count
    count = 0
    #define a and a1 
    a1 = a 
    #iterate num times
    while count <= num:
        #check for divergence
        if magnitude(a1) > 2.0:
            #return the step it diverged on 
            return count
        #iterate a
        a1 = complexAdd(complexMultiply(a1,a1),a)
        count+=1
    #if a hasn't diverged by the end
    return num

#complex numbers u=1+2i and v=3+4i
u = [1,2]
v = [3,4]
resultAdd = complexAdd(u,v)
resultMultipy = complexMultiply(u,v)
print(resultAdd, resultMultipy)

# find the magnitude of the complex number 2+i
resultMagnitude = magnitude([2,1])
print(resultMagnitude)

#Mandelbrot set  z = 0.25+1.5i
# z = [0.25,1.5]
z = [0.25,0.75]
_Multiply = complexMultiply(z,z)
_Add = complexAdd(_Multiply,z)
_Magnitude = magnitude(_Add)
print(_Multiply, _Add, _Magnitude)

_mandelbort = mandelbrot(z,10)
print()