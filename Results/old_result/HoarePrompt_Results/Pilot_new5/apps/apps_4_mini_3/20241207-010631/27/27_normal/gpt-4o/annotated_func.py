#State of the program right berfore the function call: x, y, and z are positive real numbers such that 0.1 ≤ x, y, z ≤ 200.0, and each number has exactly one digit after the decimal point.
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
#Overall this is what the function does:The function accepts three positive real numbers `x`, `y`, and `z`, each constrained between 0.1 and 200.0 with one decimal place. It evaluates various exponentiation expressions involving these numbers, finds the maximum value among them, and outputs the corresponding expression as a string. It does not return any value but prints the result directly.

