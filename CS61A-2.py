# Imports, make available, preset
from math import pi

pi * 71 / 223
from math import sin

sin(pi / 2)

# Assignment, name on the left
radius = 10
2 * radius
area, circ = pi * radius * radius, 2 * pi * radius #multiple names in one line
#area = 314.xxxxxxx
radius = 20
#area = 314.xxxxxxx, still, it is defined

# Function values
max
max(3, 4)
f = max   #max is a built-in funtion
f
f(3, 4)
max = 7   #max is a name
f(3, 4)
f(3, max) #7
f = 2
# f(3, 4)
__builtins__.max

#example
"""environmental statement and assignment statement"""
"""http://pythontutor.com/visualize.html#mode=edit, visualize process"""
"""first evaluate the operator, then the operand, 从外"""
f = min
f = max #rebind
g, h = min, max
max = g #rebind max to min function, 
"""
In [4]: max
Out[4]: <function max>
In [5]: max = g
In [6]: max
Out[6]: <function min>"""

a = max(f(2, g(h(1, 5), 3)), 4) # max-g-min, g-min, h-max, f-max(not min)
print(a)#3, h(1, 5) = 5, g(5, 3) = 3, f(2, 3) = 3, max(3, 4) = 3


# User-defined functions
from operator import add, mul


def square(x):
    return mul(x, x)

# new function
square(21)
square(add(2, 5)) #49
square(square(3)) #81


def sum_squares(x, y):
    return add(square(x), square(y)) #built-in function----add, user defined function---sq
#not yet called, no execution, just the body

sum_squares(3, 4) #25
sum_squares(5, 12)
#calling a user defined function

# area function, that is different than area =
def area():
    return pi * radius * radius


area()
radius = 20
area()
radius = 10
area()

# Name conflicts
def square(square): #def name(parameter)
    return mul(square, square)


square(4)

