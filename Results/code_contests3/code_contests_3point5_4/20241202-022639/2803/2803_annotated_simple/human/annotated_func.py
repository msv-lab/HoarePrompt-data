#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:Functionality: The function `func` reads two integers `n` and `k` from the user input. It then calculates and prints the result of 2 raised to the power of the length of the binary representation of `n`, subtracted by 1 if `k - 1` is not equal to 0; otherwise, it prints `n`. The function does not accept any parameters explicitly.

