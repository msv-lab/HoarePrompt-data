#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function reads two integers `n` and `k`, and prints \(2^{\text{len(bin(n)[2:])}} - 1\) if \(k > 1\); otherwise, it prints `n`. It does not handle invalid input or edge cases beyond the specified constraints.

