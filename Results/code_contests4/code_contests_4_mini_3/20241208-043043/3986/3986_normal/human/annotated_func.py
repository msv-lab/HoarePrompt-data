#State of the program right berfore the function call: The input consists of three positive integers representing the areas of the three faces of a rectangular parallelepiped, where each area is greater than 0 and does not exceed 10,000.
def func():
    a, b, c = map(float, raw_input().split())
    x = (a / b * c) ** 0.5
    y = (b / c * a) ** 0.5
    z = (c / a * b) ** 0.5
    print(4 * (x + y + z))
#Overall this is what the function does:The function accepts three positive integer areas representing the faces of a rectangular parallelepiped, calculates the dimensions of the parallelepiped based on these areas, and then prints four times the sum of these dimensions. However, it does not return any value; it only prints the result.

