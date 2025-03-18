#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 · 10^5.
def func_1(n):
    return sum(int(d) for d in str(n))
    #The program returns the sum of the digits of the integer `n`, where `n` is an integer such that 1 ≤ n ≤ 2 · 10^5.
#Overall this is what the function does:The function accepts an integer `n` within the range of 1 to 200,000 and returns the sum of its digits.

