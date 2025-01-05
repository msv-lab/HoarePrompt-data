#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from the input, then based on the value of `k`, it either calculates and prints 2 raised to the power of the binary length of `n` minus 1, or simply prints the value of `n`. The function does not handle the mathematical expression n choose k as described in the annotations.

