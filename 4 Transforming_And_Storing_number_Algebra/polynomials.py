from math import sqrt

def quadratic(a,b,c):
    """
    Returns the solutions of an equation of the form
    a*x**2 + b*x + c = 0
    """
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1, x2



print(quadratic(2,7,-15))