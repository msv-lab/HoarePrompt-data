#State of the program right berfore the function call: N is a non-negative integer such that 0 ≤ N ≤ 10^18, and K is a positive integer such that 1 ≤ K ≤ 10^18.
def func():
    N, K = map(int, input().split())
    print(min(N % K, K - N % K))
#Overall this is what the function does:The function reads two integers, N and K, from input, where N is a non-negative integer (0 ≤ N ≤ 10^18) and K is a positive integer (1 ≤ K ≤ 10^18). It then calculates and prints the minimum of the two values: the remainder of N divided by K (N % K) and the difference between K and that remainder (K - N % K). This effectively finds the smaller distance between N and the nearest multiples of K, either below or above N.

