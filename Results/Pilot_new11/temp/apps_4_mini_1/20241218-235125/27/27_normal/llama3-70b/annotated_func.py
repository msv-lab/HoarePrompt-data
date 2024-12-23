#State of the program right berfore the function call: x, y, and z are positive real numbers in the range [0.1, 200.0], each with exactly one digit after the decimal point.
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
#Overall this is what the function does:The function accepts three positive real numbers, x, y, and z, within the range [0.1, 200.0], each with one decimal place. It calculates twelve different power combinations of these numbers and determines which of these combinations yields the maximum value. It then prints the corresponding expression (e.g., 'x^y^z', 'y^z^x', etc.) that gave this maximum value. The function does not return any value, and it relies on standard input for its parameters. There are no checks for invalid input values or formats beyond the assumption defined in the comments before the function call. Edge cases involving very close values or rounding issues during floating-point arithmetic are not addressed.

