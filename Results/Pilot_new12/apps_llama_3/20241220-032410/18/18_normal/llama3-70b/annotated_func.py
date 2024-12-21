#State of the program right berfore the function call: n is a positive integer, k is a positive integer such that k <= n, and t is a positive integer such that 1 <= t < n + k.
def func():
    n, k, t = map(int, input().split())
    print(min(t, k) if t <= n else k - (t - n) % k)
#Overall this is what the function does:The function accepts three parameters, n, k, and t, which are positive integers where k is less than or equal to n and 1 is less than or equal to t and t is less than n + k. It calculates and prints the minimum of t and k if t is less than or equal to n; otherwise, it prints k minus the remainder of t - n divided by k. The function effectively determines the maximum number that can be achieved within the constraints of n, k, and t, adjusting according to whether t falls within the range of n or exceeds it, thus ensuring the result stays within the bounds defined by k.

