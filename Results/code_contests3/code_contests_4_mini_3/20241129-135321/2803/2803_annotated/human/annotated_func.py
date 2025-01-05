#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function reads two integers `n` and `k` from input, where 1 ≤ k ≤ n ≤ 10^18. It returns `n` if `k` is 1. If `k` is greater than 1, it computes and returns `2` raised to the number of bits in the binary representation of `n` minus 1.

