#State of the program right berfore the function call: **
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function reads three integer inputs, calculates a value based on those inputs, and prints the result after performing some mathematical operations. It does not accept any parameters and does not return any value.

