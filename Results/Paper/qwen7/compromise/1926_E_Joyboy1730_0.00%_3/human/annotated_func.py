#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * k - 1))
                break
            tot += a
            k -= tot
            pow *= 2
        
    #State: Output State: After the loop executes all its iterations, `L` will be a list containing all the values of `m` generated during each iteration, `pow` will be equal to \(2^n\) where \(n\) is the total number of iterations, `k` will be reduced to a non-positive value (since it is continuously subtracted by `tot` until it is no longer positive), `tot` will be the sum of all elements in `L`, and `m`, `n`, and `a` will be undefined.
    #
    #In natural language: After the loop has completed all its iterations, the list `L` will contain all the values of `m` that were calculated during each iteration. The variable `pow` will be \(2^n\), where \(n\) is the total number of iterations. The variable `k` will be non-positive, as it is continually reduced by `tot` until it reaches zero or becomes negative. The variable `tot` will be the sum of all elements in `L`. The variables `m`, `n`, and `a` will be undefined since they are local to the loop and are no longer in scope after the loop completes.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it calculates a sequence of integers \( m \) derived from \( n \) through repeated division by 2, and uses these values to determine a specific output based on \( k \). The function prints the result for each test case and returns nothing.

