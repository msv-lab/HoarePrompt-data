#State of the program right berfore the function call: N is a non-negative integer such that 0 ≤ N ≤ 10^{18}, K is a positive integer such that 1 ≤ K ≤ 10^{18}.
def func():
    N, K = map(int, input().split())
    print(min(N % K, K - N % K))
#Overall this is what the function does:The function reads two integers, N and K, from input, where N is a non-negative integer and K is a positive integer. It then calculates and prints the minimum of two values: the remainder of N when divided by K (N % K) and the difference between K and that remainder (K - N % K). This effectively finds the minimum distance to the nearest multiple of K from N.

