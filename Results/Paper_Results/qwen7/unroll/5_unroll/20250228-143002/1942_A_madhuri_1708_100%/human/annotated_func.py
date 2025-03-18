#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3 and the sum of n over all test cases does not exceed 10^3.
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
        
    #State: Output State: The output consists of lines where each line corresponds to a test case. If `k` is greater than or equal to 2, and `n` is equal to `k`, it prints a line with `k` occurrences of `k`. Otherwise, if `k` is less than 2, it prints a line with numbers from 1 to `n`. If `n` is not equal to `k` and `k` is at least 2, it prints `-1`. The total number of lines does not exceed 1000, corresponding to the sum of `n` over all test cases.
#Overall this is what the function does:The function processes multiple test cases, each containing two integers \( n \) and \( k \). For each test case, it prints either a line with \( k \) occurrences of \( k \) if \( n \) equals \( k \) and \( k \geq 2 \), or a line with numbers from 1 to \( n \) if \( k < 2 \). If \( n \neq k \) and \( k \geq 2 \), it prints `-1`. The total number of lines printed does not exceed 1000.

