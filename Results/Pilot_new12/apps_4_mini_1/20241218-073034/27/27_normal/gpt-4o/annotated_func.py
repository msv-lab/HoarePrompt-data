#State of the program right berfore the function call: x, y, and z are positive real numbers within the range [0.1, 200.0] and each is represented with exactly one digit after the decimal point.
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
#Overall this is what the function does:The function reads three positive real numbers (x, y, z) within the range [0.1, 200.0] from standard input. It calculates various power operations involving these numbers in different combinations, specifically assessing the results of expressions like x^y^z, (x^y)^z, etc., for all permutations of these numbers. The function then determines the maximum value from these expressions and prints the corresponding expression that yields this maximum value. The function does not return any values or take parameters, and there is no error handling for unexpected inputs or cases where inputs may not fall within the specified range. Additionally, it lacks explicit return behavior defined in the postconditions.

