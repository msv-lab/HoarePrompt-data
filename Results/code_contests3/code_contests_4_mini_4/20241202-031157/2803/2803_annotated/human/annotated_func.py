#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function reads two integers `n` and `k` from input. If `k` is greater than 1, it calculates and prints `2` raised to the power of the number of bits in the binary representation of `n`, minus 1. If `k` equals 1, it simply prints the value of `n`. This functionality handles the given constraints of `1 ≤ k ≤ n ≤ 10^18`.

