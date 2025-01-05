#State of the program right berfore the function call: **Precondition**: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from the user input, calculates a specific value based on these inputs, and then prints the result. The calculation involves determining the length of the binary representation of `n`, raising 2 to that length and subtracting 1 from the result if `k` is greater than 1, otherwise it returns `n`. The function does not have any explicit return value as it directly prints the result. However, the function is expected to handle cases where `n` and `k` are integers satisfying the condition 1 ≤ k ≤ n ≤ 10^18.

