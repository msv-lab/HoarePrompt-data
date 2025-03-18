#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: Output State: The loop will have executed all its iterations, and the final values of `n` and `k` will be those provided by the last input pair. The number of iterations left would be 0, as the loop has completed all its executions.
    #
    #In natural language, after the loop executes all its iterations, the values of `n` and `k` will be the same as the last input pair provided by the user. The loop counter will have reached zero, indicating that no more iterations are left to execute.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \) and \( k \). For each test case, it calculates and prints a value based on the given \( n \) and \( k \). If \( k = 1 \), it prints 1. If \( k \leq 2n \), it prints \( \lceil \frac{k}{2} \rceil \). Otherwise, it prints \( \frac{k}{2} + 1 \). After processing all test cases, the function ends with no return value, but the final values of \( n \) and \( k \) correspond to the last input pair provided.

