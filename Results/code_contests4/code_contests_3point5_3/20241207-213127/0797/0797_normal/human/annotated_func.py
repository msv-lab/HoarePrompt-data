#State of the program right berfore the function call: N and K are non-negative integers such that 0 <= N <= 10^18 and 1 <= K <= 10^18.**
def func():
    N, K = map(int, input().split())
    print(min(N % K, K - N % K))
#Overall this is what the function does:The function reads two non-negative integers N and K from the user input, then calculates and prints the minimum of N modulo K and K minus N modulo K. The function does not accept any parameters and does not return any specific output. It operates on the non-negative integers N and K within the specified constraints.

