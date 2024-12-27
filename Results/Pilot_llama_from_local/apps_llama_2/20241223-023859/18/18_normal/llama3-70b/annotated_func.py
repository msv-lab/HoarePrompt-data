#State of the program right berfore the function call: n is a positive integer, k is a positive integer such that k <= n, and t is a positive integer such that 1 <= t < n + k.
def func():
    n, k, t = map(int, input().split())
    print(min(t, k) if t <= n else k - (t - n) % k)
#Overall this is what the function does:The function accepts three positive integers as input: n, k, and t, where k is less than or equal to n, and t is greater than or equal to 1 and less than n + k. It then returns the minimum value between t and k if t is less than or equal to n; otherwise, it returns k minus the remainder of (t - n) divided by k. The function performs a single calculation based on the input values and prints the result, effectively providing a mathematical operation that depends on the relative values of the input parameters.

