#State of the program right berfore the function call: n and k are integers such that 1 <= k <= n <= 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function reads two integers n and k from the user input, where n and k are integers satisfying 1 <= k <= n <= 10^18. It then calculates and prints a value based on the condition: if k is not 1, it computes 2 raised to the length of the binary representation of n minus 1; otherwise, it prints n.

