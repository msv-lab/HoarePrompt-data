#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function accepts two integers `n` and `k` from input, where 1 ≤ k ≤ n ≤ 10^18. It computes and prints `n` if `k` is 1; otherwise, it calculates and prints `2` raised to the power of the length of the binary representation of `n` (excluding the '0b' prefix) minus 1. This effectively returns the maximum number of distinct non-zero values that can be formed from the bits of `n`, while also handling the special case when `k` equals 1.

