#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function `func` reads two integer inputs n and k, where 1 ≤ k ≤ n ≤ 10^18. It then calculates the number of ways to choose k items from a set of n items and prints the result.

