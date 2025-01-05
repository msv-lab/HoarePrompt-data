#State of the program right berfore the function call: **
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function `func` reads three integer inputs from the user, calculates a value based on these inputs, and prints the result. It does not return any specific output. The code does not strictly follow the postconditions mentioned in the annotations as it does not return any value explicitly. Additionally, it does not handle any potential errors or edge cases related to the input values.

