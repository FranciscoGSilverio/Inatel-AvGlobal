from sympy import Symbol, solve, tan

c = 270

def function(x):
    return (2**x) + (2 ** (4*x)) - 1 - c

x = Symbol('x')
y = function(x)
result = solve(y)

print('result: ', result)

#################################################################

def function2(w):
    return 5*(w**(1/2)) - (4 * (w**2)) + (w/2) - c

w = Symbol('w')
z = function2(w)
result2 = solve(z)

print('result2: ', result2)

#################################################################

def function3(a):
    return ((3 * tan((c - 3) * a)) + 2) ** 2

a = Symbol('a')
b = function3(a)
result3 = solve(b)

print('result3: ', result3)
