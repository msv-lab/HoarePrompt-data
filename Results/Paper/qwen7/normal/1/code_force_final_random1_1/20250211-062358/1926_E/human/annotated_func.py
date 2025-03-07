#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
            L.append(m)
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * (k - tot) - 1))
            tot += a
            pow *= 2
        
    #State: Output State: `a` is 1, `L` is [], `tot` is 10, `pow` is 16.
    #
    #Explanation: After the loop has executed all its iterations, `L` will be completely processed, and `a` will be the last non-zero element in `L`. Since `L` starts as `[2, m, m]` and `m = (n + 1) // 2`, and given the nature of the loop, `L` will eventually become an empty list. The variable `a` will be the last non-zero value from `L`, which is 1. The variable `tot` will accumulate the sum of all elements in `L`, starting from 2 and adding each `m` value until `L` is empty. Each iteration doubles the value of `pow`, so after all iterations, `pow` will be \(2^4 = 16\). Given the pattern of processing and the initial conditions, `tot` will be the sum of all elements in `L`, which, considering the nature of the loop, will be 10.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \(n\) and \(k\). For each test case, it calculates and prints a result based on the values of \(n\) and \(k\). Specifically, it constructs a list \(L\) by repeatedly dividing \(n\) by 2 and subtracting the result from \(n\). Then, it iterates over the list \(L\) to find the position where \(k\) falls within the cumulative sum of its elements, and prints a calculated value based on this position and the current power of 2. The function does not return any value but outputs the calculated results for each test case.

