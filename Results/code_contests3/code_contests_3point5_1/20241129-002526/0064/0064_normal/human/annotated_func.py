#State of the program right berfore the function call: c1, c2, c3, c4, c5 are non-negative integers such that 0 ≤ c1, c2, c3, c4, c5 ≤ 100.**
def func():
    c = map(int, raw_input().split())
    s = sum(c)
    print - 1 if s == 0 or s % len(c) != 0 else s / len(c)
#Overall this is what the function does:The function `func` reads a list of integers from the user input, calculates the sum of the integers in the list, and prints either -1 if the sum is zero or not divisible by the length of the list, or the average of the integers in the list if the sum is non-zero and divisible by the length of the list. The function does not accept any parameters and does not return any value.

