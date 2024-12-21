#State of the program right berfore the function call: x, y, and z are real numbers such that 0.1 ≤ x, y, z ≤ 200.0, and each number is represented with exactly one digit after the decimal point.
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
#Overall this is what the function does:The function takes three real numbers x, y, and z as input, ensuring they fall within the range of 0.1 to 200.0 and have one decimal place. It computes various exponentiation combinations of these numbers, specifically twelve different expressions, and determines which of these combinations results in the highest value. Finally, the function prints the corresponding mathematical expression representing this maximum value. However, the function lacks error handling for invalid inputs (e.g., non-numeric values, values outside the specified range) and assumes valid input is always provided.

