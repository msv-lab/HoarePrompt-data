#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if k % 2 == 0 and k // 2 % 2 == 1:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: The variable `t` is a positive integer such that \(0 \leq t \leq 1000\), `n` is the first integer input split from the input string, and `k` is the last integer input split from the input string after all iterations of the loop. No changes are made to `n` and `k` unless the conditions specified in the loop body are met.
#Overall this is what the function does:The function processes up to 1000 test cases, each involving two integers \(n\) and \(k\). For each test case, it calculates and prints either \(\frac{k}{2} + 1\) or \(\lceil \frac{k}{2} \rceil\) based on the condition that \(k\) is even and \(\frac{k}{2}\) is odd. After processing all test cases, the function does not return any value but prints the calculated results for each test case.

