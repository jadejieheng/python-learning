# Print
-2
print(-2)
'Go Bears'
print('Go Bears')
print(1, 2, 3)
None
print(None)
x = -2
x
x = print(-2)
x
print(print(1), print(2)) #1,2,None None

# Addition/Multiplication
from operator import add, mul
2 + 3 * 4 + 5
mul(add(2, mul(3, 4), 5))
(2 + 3) * (4 + 5)
mul(add(2, 3), add(4, 5))
pow(2,3)#2*2*2

# Division
618 / 10
618 // 10
618 % 10
from operator import truediv, floordiv, mod
floordiv(618, 10)
truediv(618, 10)
mod(618, 10)#mod

# Approximation
5 / 3#1
5 // 3#1
5 % 3#2

# Multiple return values
def divide_exact(n, d):
    return n // d, n % d
quotient, remainder = divide_exact(618, 10)#quotient bounds to 61, exact bounds to 61.8


"""def <name>(<formal parameters>):
    return <return expression>
    The second line must be indented — most programmers use four spaces to indent.
    use a function and return so that action could be repeated,
    otherwise, function is bound to a value(primitive)"""


# Dostrings, doctests, & default arguments
def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> quotient, remainder = divide_exact(618, 10)
    >>> quotient
    61
    >>> remainder
    8
    """
    return floordiv(n, d), mod(n, d)

q, r = divide_exact(2013,10)

# Conditional expressions
def absolute_value(x):
    """Return the absolute value of X.

    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x

# Summation via while
n = 3
while n >= 0:
     n -= 1
     print(n)
"""2
   1
   0
   -1 """

i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i
total #print(total)

"""
The difference is in ipython?

In [2]: total
Out[2]: 6

In [3]: print(total)
6

In [4]:

"""