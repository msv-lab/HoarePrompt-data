#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: Output State: The output state will consist of a series of integers printed based on the conditions given within the loop. For each test case, if \( k = 1 \), it will print 1. If \( k \leq 2(n + (n - 2)) \), it will print \( \lceil \frac{k}{2} \rceil \). Otherwise, it will print \( \frac{k}{2} + 1 \).
    #
    #This output state will be determined by the values of \( n \) and \( k \) entered for each test case during the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \) and \( k \). For each test case, it prints an integer based on specific conditions: if \( k = 1 \), it prints 1; if \( k \leq 2(n + (n - 2)) \), it prints \( \lceil \frac{k}{2} \rceil \); otherwise, it prints \( \frac{k}{2} + 1 \). The function does not return any value but outputs a series of integers corresponding to the conditions evaluated for each test case.

