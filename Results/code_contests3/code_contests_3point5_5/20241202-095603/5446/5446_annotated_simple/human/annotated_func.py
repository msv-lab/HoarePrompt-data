#State of the program right berfore the function call: **
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function `func` reads three integer inputs, calculates a value based on the inputs, and prints the result after some mathematical operations. The function does not accept any parameters explicitly, but it reads input from the user during execution. It calculates a value based on the input and prints the result.

