#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function `func` reads two integers `n` and `k`, where 1 ≤ k ≤ n ≤ 10^18. It then performs a mathematical operation and prints the result. If k is greater than 1, it calculates 2 to the power of the length of the binary representation of n, subtracts 1 from it, and prints the result. If k is 1, it directly prints the value of n. Therefore, the functionality of the function is to calculate and print a specific mathematical operation based on the values of n and k.

