#State of the program right berfore the function call: The input consists of three space-separated integers representing the areas of the three faces of a rectangular parallelepiped. The areas are positive integers not exceeding 10^4.**
def func():
    a, b, c = map(float, raw_input().split())
    x = (a / b * c) ** 0.5
    y = (b / c * a) ** 0.5
    z = (c / a * b) ** 0.5
    print(4 * (x + y + z))
#Overall this is what the function does:The function `func` reads three space-separated integers as input representing the areas of the three faces of a rectangular parallelepiped. It then calculates the square roots of specific area ratios and prints the result of a mathematical operation involving these square roots. The function does not return any value.

