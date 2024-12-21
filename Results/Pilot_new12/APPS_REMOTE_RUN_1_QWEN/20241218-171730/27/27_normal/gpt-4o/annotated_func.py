#State of the program right berfore the function call: x, y, and z are real numbers with exactly one digit after the decimal point, ranging from 0.1 to 200.0 inclusive.
def func_1():
    input = sys.stdin.read
    x, y, z = map(float, input().split())
    expressions = [(x ** y ** z, 'x^y^z'), (x ** z ** y, 'x^z^y'), ((x ** y) **
    z, '(x^y)^z'), ((x ** z) ** y, '(x^z)^y'), (y ** x ** z, 'y^x^z'), (y **
    z ** x, 'y^z^x'), ((y ** x) ** z, '(y^x)^z'), ((y ** z) ** x, '(y^z)^x'
    ), (z ** x ** y, 'z^x^y'), (z ** y ** x, 'z^y^x'), ((z ** x) ** y,
    '(z^x)^y'), ((z ** y) ** x, '(z^y)^x')]
    max_value, max_expr = max(expressions, key=lambda pair: pair[0])
    print(max_expr)
#Overall this is what the function does:The function does not accept any parameters and processes three real numbers \(x\), \(y\), and \(z\) with exactly one digit after the decimal point, ranging from 0.1 to 200.0 inclusive. It calculates 12 different expressions involving exponentiation of these numbers in various orders. After computing these expressions, it determines the maximum value among them and prints the expression corresponding to this maximum value. The function handles all valid inputs within the specified range and does not account for invalid inputs such as non-real numbers or values outside the specified range. If multiple expressions have the same maximum value, the function will print one of them arbitrarily.

