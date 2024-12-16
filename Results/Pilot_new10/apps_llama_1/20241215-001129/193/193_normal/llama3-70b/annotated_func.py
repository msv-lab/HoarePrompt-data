#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print(abs(x - y))
#Overall this is what the function does:The function reads two integer inputs from the user, calculates the absolute difference between them, and prints the result, without enforcing any specific range or relationship between the input values, and without returning any value.

