
from math import floor, ceil

def clamp(value, lower, upper):
    return lower if value < lower else upper if value > upper else value

def lerp(a, b, t):
    #Linearly interpolates between a and b by t.
    return a + (b-a) * clamp(t, 0, 1)


def inverse_lerp(a, b, value):
    #Calculates the linear parameter t that produces the interpolant value within the range [a, b].
    if a != b:
        return clamp((value - a) / (b - a), 0 ,1)
    else:
        return 0

def roundDown(n, d=8):
    d = int('1' + ('0' * d))
    return floor(n * d) / d

def roundUp(n, d=8):
    d = int('1' + ('0' * d))
    return ceil(n * d) / d
