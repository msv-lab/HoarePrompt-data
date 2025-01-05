#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ k ≤ n ≤ 10^18.
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function reads two positive integers `n` and `k` from input, where `1 ≤ k ≤ n ≤ 10^18`. It computes and prints `n` if `k` is 1. If `k` is greater than 1, it calculates and prints `2` raised to the power of the number of bits in the binary representation of `n` (excluding the '0b' prefix) minus 1. This effectively gives the maximum number of subsets of a set of size `n` minus one.

