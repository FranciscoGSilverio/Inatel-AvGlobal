from sympy import Limit, Symbol, S

c = 270

def lim1(x):
    return (1 + ((c + 4) / x**3)) ** (x**3)

x = Symbol('x')

Result1 = Limit(lim1(x), x, 0).doit()

print('Resutado 1', Result1)

Result2 = Limit(lim1(x), x, S.Infinity).doit()

print('Resutado 2', Result2)

Result3 = Limit(lim1(x), x, -S.Infinity).doit()

print('Resutado 3', Result3)
