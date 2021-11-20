
"""
SOLVING FIRST-DEGREE EQUATION
"""
def f(x):
    return 2*x + 5 

def plug_f():
    x = -100
    while x < 100:
        if f(x) == 13:
            print("x =", x)
        x += 1

plug_f()



"""
USING PLUG() TO SOLVE A CUBIC EQUATION
"""
def g(x):
    return 6*x**3+31*x**2+3*x-10

def plug_g():
    x = -100
    while x < 100:
        if g(x) == 0:
            print("x =", x)
        x +=1
    print("done.")

plug_g()

