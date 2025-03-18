#State of the program right berfore the function call: x, y, and z are positive real numbers in the range [0.1, 200.0] with exactly one digit after the decimal point.
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
#Overall this is what the function does:The function accepts three positive real numbers `x`, `y`, and `z` (each in the range [0.1, 200.0] with one digit after the decimal point) and calculates various expressions of the form `a^b^c` and `((a^b)^c)`, for all permutations of `x`, `y`, and `z`. It then determines and outputs the expression that results in the maximum value among these calculations. The function does not handle any potential input errors or validations, relying on the assumption that the input format will always be correct.

