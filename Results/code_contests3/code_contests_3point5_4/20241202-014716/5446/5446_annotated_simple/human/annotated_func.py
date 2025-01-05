#State of the program right berfore the function call: **Precondition**: **a, b, and n are integers such that 1 ≤ a, b ≤ 100, 2 ≤ n ≤ a + b.**
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function reads three integers as input, calculates a value based on those inputs, and then prints the result after performing some mathematical operations. The function calculates the division between the maximum and minimum of two of the input values, multiplies it by the division of the minimum value by another input, and then prints the integer value of the result after the division.

