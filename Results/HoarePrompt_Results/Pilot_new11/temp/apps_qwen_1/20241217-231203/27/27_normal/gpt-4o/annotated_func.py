#State of the program right berfore the function call: x, y, and z are real numbers with exactly one digit after the decimal point, such that 0.1 ≤ x, y, z ≤ 200.0.
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
#Overall this is what the function does:The function reads three real numbers \(x\), \(y\), and \(z\) from standard input, where each number has exactly one digit after the decimal point and lies within the range \([0.1, 200.0]\). It then calculates 12 different mathematical expressions involving exponentiation of these numbers in various orders. The function determines which of these expressions yields the maximum value and prints the corresponding expression string. The function does not accept any parameters and does not return any value.

