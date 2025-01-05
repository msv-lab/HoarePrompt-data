#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function `func` reads two integers n and k from the input, where 1 ≤ k ≤ n ≤ 10^18. It then prints a value based on the following logic: if k - 1 is not equal to 0, it calculates 2 raised to the length of the binary representation of n minus 1; otherwise, it prints n. The function does not accept any parameters explicitly but relies on the user providing n and k through input.

