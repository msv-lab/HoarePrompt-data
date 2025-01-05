#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function `func` reads two positive integers `n` and `k` from the input, and based on the value of `k`, it either calculates and prints the number of ways to choose `k` items from `n` items without replacement using a mathematical formula or prints `n`. The function does not accept any parameters explicitly, and the parameters `n` and `k` are positive integers such that 1 <= k <= n <= 10^18.

