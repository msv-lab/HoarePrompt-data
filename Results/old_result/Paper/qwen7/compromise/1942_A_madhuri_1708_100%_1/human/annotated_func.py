#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are positive integers such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[(j + 1) for j in range(n)])
        
    #State: Output State: The output will consist of lines where each line corresponds to a test case. If `k` is greater than or equal to 2, and `n` is equal to `k`, the line will contain `k` occurrences of `k`. Otherwise, if `k` is less than 2 or `n` is not equal to `k`, the line will contain `-1`. If `k` is 1, the line will contain numbers from 1 to `n`.
    #
    #For example, if there are two test cases with inputs:
    #1. `n = 3, k = 3`
    #2. `n = 4, k = 1`
    #
    #The output will be:
    #```
    #3 3 3
    #1 2 3 4
    #```
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). It reads these integers from standard input, checks the relationship between \( n \) and \( k \), and prints either a sequence of \( k \) occurrences of \( k \) (if \( n = k \) and \( k \geq 2 \)), a sequence of numbers from 1 to \( n \) (if \( k = 1 \)), or -1 (otherwise). The output is printed to standard output, with each line corresponding to one test case.

