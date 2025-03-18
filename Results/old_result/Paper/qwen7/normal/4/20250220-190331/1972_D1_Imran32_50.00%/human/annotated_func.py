#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6, and the sum of all n and the sum of all m over all test cases do not exceed 2⋅10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` is an integer, `k` is an integer, `ans` is equal to `n + sum((n + i) // (i * i) for i in range(2, root + 1))`, `root` is at least 2, and `i` is `root + 1`.
    #
    #In simpler terms, after the loop has executed all its iterations, `t` remains within the range of 1 to \(10^4\), `n` and `k` remain as they were initially, and `ans` is updated to include the sum of \((n + i) // (i * i)\) for each `i` starting from 2 up to `root + 1`. The value of `root` is at least 2, and the last value of `i` used in the loop is `root + 1`.
    print(ans)
    #This is printed: n + sum((n + i) // (i * i) for i in range(2, root + 1))
#Overall this is what the function does:The function processes a series of test cases, where each test case includes two positive integers \(n\) and \(m\). It calculates and prints the value of \(n + \sum_{i=2}^{\text{root}} \left(\frac{n + i}{i^2}\right)\), where \(\text{root}\) is defined as \(\sqrt{n} + 1\). The function reads \(n\) and \(k\) from input, although \(k\) is not used in the calculation. After processing all test cases, it outputs the calculated value for each test case.

