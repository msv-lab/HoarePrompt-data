#State of the program right berfore the function call: The input is a string containing three space-separated real numbers x, y, and z, each with exactly one digit after the decimal point, such that 0.1 <= x, y, z <= 200.0.
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
#Overall this is what the function does:The function accepts an input string of three space-separated real numbers from the standard input, calculates twelve different exponentiation expressions, and prints the string representation of the expression that results in the maximum value, assuming the input is well-formed and within a specified range, without explicit handling for potential edge cases such as invalid input formats or out-of-range values.

