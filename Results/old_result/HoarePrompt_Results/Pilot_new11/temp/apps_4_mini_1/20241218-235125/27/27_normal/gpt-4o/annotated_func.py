#State of the program right berfore the function call: x, y, and z are positive real numbers in the range [0.1, 200.0], each with exactly one digit after the decimal point.
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
#Overall this is what the function does:The function reads three positive real numbers, x, y, and z, from standard input, each within the range [0.1, 200.0] and with exactly one digit after the decimal point. It evaluates a series of power expressions formed from these three numbers and determines the maximum value among them. The function then prints the expression that corresponds to this maximum value. Note that the function does not handle invalid inputs or any edge cases such as exceptions caused by reading from input. Additionally, it does not return a value; it solely prints the result.

