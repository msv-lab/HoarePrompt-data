#State of the program right berfore the function call: x, y, and z are positive real numbers within the range [0.1, 200.0], each expressed with exactly one digit after the decimal point.
def func():
    x, y, z = map(float, input().split())
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
    b = ['x^y^z', 'x^z^y', '(x^y)^z', '(x^z)^y', 'y^x^z', 'y^z^x', '(y^x)^z',
    '(y^z)^x', 'z^x^y', 'z^y^x', '(z^x)^y', '(z^y)^x']
    print(b[a.index(max(a))])
#Overall this is what the function does:The function accepts three positive real numbers `x`, `y`, and `z`, each within the range [0.1, 200.0] with one digit after the decimal point. It calculates 12 different power expressions involving these three numbers and identifies the expression that results in the maximum value. The function then prints the corresponding mathematical expression associated with that maximum value. The function does not explicitly return any value.

