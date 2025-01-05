#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from the input, where 1 ≤ k ≤ n ≤ 10^18. It then computes and prints a value based on the condition: if k - 1 is true, it prints the result of 2 raised to the length of the binary representation of n minus 1; otherwise, it prints n. The function does not have a return value.

