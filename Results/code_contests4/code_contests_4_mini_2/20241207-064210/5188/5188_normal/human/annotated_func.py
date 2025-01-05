#State of the program right berfore the function call: a and b are integers such that 1 ≤ a, b ≤ 10^9.
def func_1(a, b):
    if (a > b) :
        return a - b
        #The program returns the difference between integer 'a' (which is greater than 'b') and integer 'b', resulting in a positive integer value.
    #State of the program after the if block has been executed: *`a` and `b` are integers such that 1 ≤ `a`, `b` ≤ 10^9, and `a` is less than or equal to `b`.
    return b - a
    #The program returns the difference between integers `b` and `a`, where `1 ≤ a ≤ b ≤ 10^9`.
#Overall this is what the function does:The function accepts two integer parameters `a` and `b`, and returns the absolute difference between `a` and `b`. If `a` is greater than `b`, it returns `a - b`; otherwise, it returns `b - a`. The result is always a non-negative integer, as it effectively calculates `|a - b|`.

