#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: Output State: The output state will consist of a series of lines, each containing either "1" or "n - 1", where "n" and "k" are integers provided by the user for each iteration of the loop. For each iteration, if "k" is greater than or equal to "n - 1", the line will contain "1"; otherwise, it will contain "n - 1". The number of lines will be equal to the value of "t".
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers `n` and `k`. If `k` is greater than or equal to `n - 1`, it prints `1`; otherwise, it prints `n - 1`. This process is repeated `t` times, where `t` is the number of test cases provided by the user. The function does not return any value but outputs the results for each test case.

