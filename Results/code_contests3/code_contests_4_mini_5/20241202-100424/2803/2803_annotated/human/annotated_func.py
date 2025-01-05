#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function reads two integers, `n` and `k`, from input, where `1 ≤ k ≤ n ≤ 10^18`. If `k` is greater than 1, it calculates and returns `2` raised to the power of the number of bits in `n` minus 1. If `k` is equal to 1, it simply returns `n`. The function does not accept any parameters and executes based on input values.

