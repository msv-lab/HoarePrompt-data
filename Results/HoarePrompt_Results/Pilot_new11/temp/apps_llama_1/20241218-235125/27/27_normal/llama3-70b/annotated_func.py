#State of the program right berfore the function call: x, y, and z are positive real numbers between 0.1 and 200.0 (inclusive) with exactly one digit after the decimal point.
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
#Overall this is what the function does:The function implicitly accepts three positive real numbers x, y, and z as input, each between 0.1 and 200.0 with one digit after the decimal point, calculates twelve different exponential expressions using these numbers, and prints the string representation of the expression that yields the maximum value. However, the function does not handle potential edge cases such as non-numeric input, input values outside the specified range, or input values with more or less than one digit after the decimal point. Additionally, the function does not return any value, instead, it prints the result directly. The state of the program after it concludes will be the printing of the expression that resulted in the maximum calculated value among the twelve exponential expressions, without any explicit error handling or return value.

