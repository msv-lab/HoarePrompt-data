#State of the program right berfore the function call: c1, c2, c3, c4, c5 are integers such that 0 <= c1, c2, c3, c4, c5 <= 100.**
def func():
    c = map(int, raw_input().split())
    s = sum(c)
    print - 1 if s == 0 or s % len(c) != 0 else s / len(c)
#Overall this is what the function does:The function `func` reads integers from user input, calculates the sum of those integers, and prints the average of the integers if the sum is not zero and divisible by the count of integers. It does not accept any parameters and does not return any value.

