#State of the program right berfore the function call: c1, c2, c3, c4, c5 are integers such that 0 <= c1, c2, c3, c4, c5 <= 100.**
def func():
    c = map(int, raw_input().split())
    s = sum(c)
    print - 1 if s == 0 or s % len(c) != 0 else s / len(c)
#Overall this is what the function does:The function `func` reads a list of integers from the user input, calculates the sum of the integers, and prints either -1, the average of the integers, or the sum of the integers divided by the number of integers in the list based on specific conditions. It does not have any actual return value. The function operates without any input parameters and outputs the result to the console.

