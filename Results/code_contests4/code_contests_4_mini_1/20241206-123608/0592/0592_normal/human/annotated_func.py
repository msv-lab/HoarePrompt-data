#State of the program right berfore the function call: a and b are distinct positive integers such that 1 ≤ a, b ≤ 10^6.
def func_1(a, b):
    return a if b == 0 else func_1(b, a % b)
    #The program returns the value of 'a' if 'b' is 0; otherwise, it calls 'func_1' with 'b' and the remainder of 'a' divided by 'b' (a % b)
#Overall this is what the function does:The function accepts two distinct positive integers `a` and `b`, and it computes the greatest common divisor (GCD) of `a` and `b` using the Euclidean algorithm. It returns `a` if `b` is 0; otherwise, it recursively calls itself with `b` and the remainder of `a` divided by `b` (i.e., `a % b`). This process continues until one of the numbers becomes zero, at which point the other number is the GCD.

