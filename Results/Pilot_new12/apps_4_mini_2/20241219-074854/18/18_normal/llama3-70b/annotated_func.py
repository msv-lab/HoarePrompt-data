#State of the program right berfore the function call: n, k, and t are positive integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    print(min(t, k) if t <= n else k - (t - n) % k)
#Overall this is what the function does:The function reads three positive integers n, k, and t from input, where 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. It computes a result based on the value of t in relation to n and k. Specifically, if t is less than or equal to n, it outputs the minimum of t and k. If t is greater than n, it calculates k minus the remainder of (t - n) divided by k, effectively determining the equivalent position in a repeating sequence modulated by k. The function does not return a value but instead directly prints the result to the output. This logic encompasses all described conditions, ensuring edge cases where t is equal to or less than n and greater than n are handled appropriately.

