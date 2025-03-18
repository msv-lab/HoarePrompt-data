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
        
    #State: All possible outputs based on the given conditions have been printed.
#Overall this is what the function does:The function processes input data from standard input, where each line contains two integers \(n\) and \(k\) separated by spaces. It prints a sequence of numbers based on the values of \(n\) and \(k\). If \(k \geq 2\) and \(n = k\), it prints \(k\) occurrences of \(k\). If \(k \geq 2\) and \(n \neq k\), it prints \(-1\). If \(k < 2\), it prints the sequence of numbers from 1 to \(n\). After processing all lines of input, the function concludes with all possible outputs printed.

