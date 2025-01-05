#State of the program right berfore the function call: **
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function `func` reads three integer values from user input, calculates a result based on these values, and prints the result. It does not accept any parameters and does not have a return value. The code calculates a value based on the input integers and prints the result.

