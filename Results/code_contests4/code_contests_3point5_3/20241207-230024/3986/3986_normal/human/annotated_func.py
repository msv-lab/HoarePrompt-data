#State of the program right berfore the function call: The input consists of three space-separated integers representing the areas of the three faces of a rectangular parallelepiped.**
def func():
    a, b, c = map(float, raw_input().split())
    x = (a / b * c) ** 0.5
    y = (b / c * a) ** 0.5
    z = (c / a * b) ** 0.5
    print(4 * (x + y + z))
#Overall this is what the function does:The function `func` takes three space-separated integers as input representing the areas of the three faces of a rectangular parallelepiped. It then calculates the square roots of the ratios of these areas and assigns them to variables x, y, and z respectively. Finally, it prints the result of 4 times the sum of x, y, and z. The function does not explicitly return any value.

