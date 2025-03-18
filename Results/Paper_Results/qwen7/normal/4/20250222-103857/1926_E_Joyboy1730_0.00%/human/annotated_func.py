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
        
    #State: Output State: `L` contains at least `t` elements, `pow` is equal to \(2^t\), `tot` is the sum of all elements in `L`, and `k` is reduced to a value that is no longer less than or equal to the sum of any remaining elements in `L`.
    #
    #In natural language: After the loop executes all its iterations, `L` will contain at least as many elements as the input integer `t`. The variable `pow` will be equal to \(2^t\) because it doubles with each iteration of the loop. `tot` will be the sum of all elements in the list `L` since it accumulates the values of `a` in each iteration. Finally, `k` will be reduced to a value that is no longer less than or equal to the sum of any remaining elements in `L`, meaning that the loop has processed all elements in `L` and `k` has been fully consumed or adjusted according to the loop's logic.
#Overall this is what the function does:The function processes multiple test cases, each containing two integers \(n\) and \(k\). For each test case, it calculates a value based on the relationship between \(n\) and \(k\) and prints the result. After processing all test cases, it outputs a series of values derived from the given inputs, ensuring that \(k\) is fully consumed or adjusted according to the loop's logic. The final state includes a list \(L\) containing at least \(t\) elements, where \(t\) is the number of test cases, and the variable \(pow\) is set to \(2^t\).

