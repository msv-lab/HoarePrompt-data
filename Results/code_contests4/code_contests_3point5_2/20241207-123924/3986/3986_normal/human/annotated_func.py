#State of the program right berfore the function call: The input consists of three space-separated integers representing the areas of the three faces of a rectangular parallelepiped. The area's values are positive (>0) and do not exceed 10^4.**
def func():
    a, b, c = map(float, raw_input().split())
    x = (a / b * c) ** 0.5
    y = (b / c * a) ** 0.5
    z = (c / a * b) ** 0.5
    print(4 * (x + y + z))
#Overall this is what the function does:The function `func` reads three space-separated integers representing the areas of the three faces of a rectangular parallelepiped, calculates the square roots of the products of pairs of these areas, and then prints the sum of these square roots multiplied by 4. The function assumes the input areas are positive (>0) and do not exceed 10^4.

