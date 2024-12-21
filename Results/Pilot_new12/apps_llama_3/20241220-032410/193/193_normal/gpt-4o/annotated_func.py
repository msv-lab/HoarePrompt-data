#State of the program right berfore the function call: x and y are integers such that 3 <= y < x <= 100,000, where x is the starting side length of an equilateral triangle and y is the ending side length of an equilateral triangle.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function takes two integers as input, representing the starting and ending side lengths of equilateral triangles, calculates and prints the ceiling of half the difference between the two side lengths, effectively rounding up to the nearest whole number if the difference is odd, and does not return any value (i.e., implicitly returns None), with the program state being modified by the input and output operations, and the calculated result being printed to the console, without any error handling or validation for the input values beyond what is implicitly enforced by the input and calculation operations.

