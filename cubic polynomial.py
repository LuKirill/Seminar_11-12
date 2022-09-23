# f(x) = 18x^3+5x^2 + 10x - 30
#
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

from sympy import *
import re

cu_po = "f(x) = 18x^3+5x^2 + 10x - 30"
cu = re.sub(r'[a-z]|[()=+*^/-]', ' ', cu_po)
a = int(re.split(r'\s+?(\d+?)\s+?\d\s+?\d+?\s+?\d\s+?\d+?\s+?\d+', cu)[1])
b = int(re.split(r'\s+?\d+?\s+?\d\s+?(\d+?)\s+?\d\s+?\d+?\s+?\d+', cu)[1])
c = int(re.split(r'\s+?\d+?\s+?\d\s+?\d+?\s+?\d\s+?(\d+?)\s+?\d+', cu)[1])
d = int(re.split(r'\s+?\d+?\s+?\d\s+?\d+?\s+?\d\s+?\d+?\s+?(\d+)', cu)[1])
print("Определим корни: f(x)=18x^3+5x^2+10x-30")
x = Symbol('x')
print(f'a={a}, b={b}, c={c}, d={d}')
x_lib = solve(a * x ** 3 + b * x ** 2 + c * x - d, x)
for i in x_lib:
    print(i.evalf())

f = a * x ** 3 + b * x ** 2 + c * x - d
fp = diff(f)
print(fp)
fp = solve(fp, x)
for j in fp:
    print(j.evalf())
