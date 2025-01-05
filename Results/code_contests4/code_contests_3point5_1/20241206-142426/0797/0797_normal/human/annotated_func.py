#State of the program right berfore the function call: N and K are non-negative integers such that 0 ≤ N ≤ 10^{18} and 1 ≤ K ≤ 10^{18}.**
def func():
    N, K = map(int, input().split())
    print(min(N % K, K - N % K))
#Overall this is what the function does:The function `func` reads two non-negative integers N and K from the input, where 0 ≤ N ≤ 10^18 and 1 ≤ K ≤ 10^18. It then calculates and prints the minimum value between N % K and K - N % K. The function does not accept any parameters and performs this calculation based on the input constraints.

