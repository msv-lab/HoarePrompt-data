#State of the program right berfore the function call: n and k are integers such that 1 <= k <= n <= 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from the user input, then calculates and prints a value based on the conditions provided. If `k` is not equal to 1, it calculates `2` to the power of the length of the binary representation of `n`, subtracts `1` from it, and prints the result. Otherwise, if `k` is equal to 1, it simply prints the value of `n`. The function does not return any value.

