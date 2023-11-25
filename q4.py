from sympy import symbols, Eq, solve

c = 270 % 10

I1, I2, I3 = symbols('I1 I2 I3')

V1 = (c + 2) * 4
V2 = (c + 1) * 5

R1, R2, R3 = 12, 4, 6

exp1 = Eq(I1, I2 + I3)
exp2 = Eq(V1, I1*R1 + I3*R3)
exp3 = Eq(V2, I2*R2 - I3*R3)

solutions = solve((exp1, exp2, exp3),(I1,I2, I3))

print (solutions)