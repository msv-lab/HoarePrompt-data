#State of the program right berfore the function call: The input contains three space-separated real numbers x, y, and z, each with exactly one digit after the decimal point, such that 0.1 <= x, y, z <= 200.0.
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
#Overall this is what the function does:The function accepts three space-separated real numbers x, y, and z as input, calculates 12 different expressions involving exponentiation of these numbers, and returns the string representation of the expression that results in the maximum value. The input numbers x, y, and z are expected to be in the range 0.1 <= x, y, z <= 200.0, each with exactly one digit after the decimal point. The function performs no error checking or handling for invalid inputs, such as non-numeric input, numbers outside the specified range, or incorrect formatting. The output will be one of the 12 predefined expressions, without considering any potential edge cases or missing logic, such as division by zero (which is not applicable in this case), overflow, or underflow. The function does not modify the input variables and only prints the result to the console, leaving the state of the program unchanged except for the printed output.

