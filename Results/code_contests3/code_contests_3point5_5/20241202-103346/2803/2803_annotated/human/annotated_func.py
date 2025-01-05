#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from the user input, where 1 ≤ k ≤ n ≤ 10^18. It then prints the result of a bitwise operation based on the values of `n` and `k`. If `k - 1` evaluates to True, it calculates and prints `2

