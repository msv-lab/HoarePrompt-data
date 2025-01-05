#State of the program right berfore the function call: The input consists of three positive integers representing the areas of the three faces of a rectangular parallelepiped, each area value is greater than 0 and does not exceed 10^4.
def func():
    a, b, c = map(float, raw_input().split())
    x = (a / b * c) ** 0.5
    y = (b / c * a) ** 0.5
    z = (c / a * b) ** 0.5
    print(4 * (x + y + z))
#Overall this is what the function does:The function accepts three positive float parameters representing the areas of the three faces of a rectangular parallelepiped (a, b, c). It calculates the lengths of the edges (x, y, z) based on these areas and returns the total surface area of the parallelepiped by printing 4 times the sum of these lengths. The function does not return a value but instead prints the result directly.

