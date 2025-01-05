#State of the program right berfore the function call: The input consists of three positive integers representing the areas of the parallelepiped's faces, where each area is greater than 0 and does not exceed 10,000.
def func():
    a, b, c = map(float, raw_input().split())
    x = (a / b * c) ** 0.5
    y = (b / c * a) ** 0.5
    z = (c / a * b) ** 0.5
    print(4 * (x + y + z))
#Overall this is what the function does:The function accepts three positive floating-point numbers representing the areas of a parallelepiped's faces, calculates the semi-axes lengths (x, y, z) based on the provided areas, and prints four times the sum of these lengths. It does not return any value and does not handle invalid input or check if the areas are valid for forming a parallelepiped.

