#State of the program right berfore the function call: N and K are integers such that 0 ≤ N ≤ 10^{18} and 1 ≤ K ≤ 10^{18}.
def func():
    N, K = map(int, input().split())
    print(min(N % K, K - N % K))
#Overall this is what the function does:The function accepts two integers, N and K, where N is in the range [0, 10^{18}] and K is in the range [1, 10^{18}]. It computes the minimum of the two values: the remainder of N divided by K and the difference between K and that remainder. The function does not return a value but prints this minimum to the output.

