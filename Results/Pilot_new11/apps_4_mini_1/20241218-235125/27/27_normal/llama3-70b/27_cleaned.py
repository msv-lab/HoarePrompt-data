(x, y, z) = map(float, input().split())
a1 = x ** y ** z
a2 = x ** z ** y
a3 = (x ** y) ** z
a4 = (x ** z) ** y
a5 = y ** x ** z
a6 = y ** z ** x
a7 = (y ** x) ** z
a8 = (y ** z) ** x
a9 = z ** x ** y
a10 = z ** y ** x
a11 = (z ** x) ** y
a12 = (z ** y) ** x
a = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
b = ['x^y^z', 'x^z^y', '(x^y)^z', '(x^z)^y', 'y^x^z', 'y^z^x', '(y^x)^z', '(y^z)^x', 'z^x^y', 'z^y^x', '(z^x)^y', '(z^y)^x']
print(b[a.index(max(a))])