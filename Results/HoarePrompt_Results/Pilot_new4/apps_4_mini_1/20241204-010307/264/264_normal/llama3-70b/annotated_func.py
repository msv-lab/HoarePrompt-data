#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, m is a positive integer such that 1 <= m <= 10,000, and a_i are positive integers such that 1 <= a_i <= 100 for i from 1 to n.
def func():
    n = int(input())
    m = int(input())
    a = [int(input()) for _ in range(n)]
    min_k = max(a) + (m + n - 1) // n
    max_k = max(a) + m
    print(min_k, max_k)
#Overall this is what the function does:The function accepts no parameters directly but reads input values for a positive integer `n` (where 1 <= n <= 100), a positive integer `m` (where 1 <= m <= 10,000), and a list of positive integers `a_i` (where 1 <= a_i <= 100 for i from 1 to n). It calculates `min_k` as the maximum value in the list `a` plus the ceiling of `m/n`, and `max_k` as the maximum value in `a` plus `m`. Finally, it prints the values of `min_k` and `max_k`. The function does not return any values.

