#State of the program right berfore the function call: c1, c2, c3, c4, and c5 are non-negative integers where 0 ≤ c1, c2, c3, c4, c5 ≤ 100.**
def func():
    c = map(int, raw_input().split())
    s = sum(c)
    print - 1 if s == 0 or s % len(c) != 0 else s / len(c)
#Overall this is what the function does:The function `func` reads a line of integers separated by spaces, calculates the sum of those integers, and prints either -1 if the sum is 0 or not divisible evenly by the number of integers, or the average of the sum if it is divisible evenly by the number of integers. The function does not accept any parameters and operates solely based on the input given.

