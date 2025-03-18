#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if k % 2 == 0 and k // 2 % 2 == 1:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: Output State: The variable `t` remains a positive integer such that \(1 \leq t \leq 1000\), `_` is set to `t-1` after the loop completes, `n` retains its value from the first input, and `k` retains its value from the last input provided during the loop's iterations. No further changes are made to these variables within the loop, so their values persist based on the last inputs received.
    #
    #In simpler terms, after the loop finishes executing all its iterations, `t` will still be within the range of 1 to 1000, `_` will be equal to the total number of iterations minus one (i.e., `t-1`), `n` will be the `n` value from the first input, and `k` will be the `k` value from the last input processed by the loop.
#Overall this is what the function does:The function processes up to 1000 test cases, each consisting of integers n and k. For each test case, it calculates and prints either k // 2 + 1 or ceil(k / 2) based on the parity conditions of k. After processing all test cases, the function does not return any value but prints the results for each test case.

