#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function takes two integers as input from the user, calculates and prints the ceiling of their difference divided by 2, without returning any value. It implicitly expects the input integers to adhere to the constraints 3 ≤ y < x ≤ 100,000, but does not enforce these constraints within the function itself. The function's output will be an integer representing this calculated value, which can range from 1 to 49999, given the input constraints. The state of the program after conclusion will have the input values stored in variables x and y, and the calculated result printed to the console, but the original input values remain unchanged.

