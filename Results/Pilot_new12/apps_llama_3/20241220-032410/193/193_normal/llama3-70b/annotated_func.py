#State of the program right berfore the function call: The function takes no parameters, but the input contains two integers x and y (3 ≤ y < x ≤ 100 000) representing the starting and ending equilateral triangle side lengths respectively.
def func():
    x, y = map(int, input().split())
    print(abs(x - y))
#Overall this is what the function does:The function takes two integers as input, representing the starting and ending equilateral triangle side lengths, and prints the absolute difference between these two integers. The function assumes that the input integers are provided in a single line separated by a space, and the program terminates after printing the result without returning any value. The function does not validate the input range defined by the annotations (3 ≤ y < x ≤ 100 000), so it will work with any two integers. The function does not perform any triangle-related calculations or checks, it simply calculates the absolute difference between the two input integers.

