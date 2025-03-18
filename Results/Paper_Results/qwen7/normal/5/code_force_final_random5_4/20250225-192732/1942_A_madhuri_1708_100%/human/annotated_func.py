#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
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
        
    #State: All lines from the input file (or standard input) have been processed, and the loop has terminated.
#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case consists of integers \(n\) and \(k\). It prints either a sequence of integers from 1 to \(n\) or \(-1\) based on the values of \(n\) and \(k\). Specifically, if \(k \geq 2\), it prints a sequence of \(k\) repeated \(k\) times only if \(n = k\); otherwise, it prints \(-1\). If \(k < 2\), it prints a sequence of integers from 1 to \(n\). After processing all test cases, the function terminates.

