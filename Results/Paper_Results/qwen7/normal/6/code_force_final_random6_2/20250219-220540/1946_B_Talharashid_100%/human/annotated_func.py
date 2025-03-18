#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 \cdot 10^5, and the sum of the values of n and k for all test cases does not exceed 2 \cdot 10^5. a is a list of n integers where each integer a_i satisfies -10^9 ≤ a_i ≤ 10^9.
def func():
    for i in range(int(input())):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        c = 0
        
        maxi = 0
        
        for ele in l:
            if ele < 0 and c <= abs(ele):
                maxi = max(c, maxi)
                c = 0
            else:
                c += ele
                maxi = max(c, maxi)
        
        maxi = max(c, maxi)
        
        print((2 ** k * maxi - maxi + sum(l)) % 1000000007)
        
    #State: Output State: The output state after the loop executes all the iterations is as follows: `t` is a positive integer such that \(1 \leq t \leq 10^4\). For each test case, `n` and `k` are positive integers such that \(1 \leq n, k \leq 2 \cdot 10^5\), and the sum of the values of `n` and `k` for all test cases does not exceed \(2 \cdot 10^5\). `a` is a list of `n` integers where each integer `a_i` satisfies \(-10^9 \leq a_i \leq 10^9\). `c` is the final cumulative value of `c` based on the conditions inside the loop for all iterations. `maxi` is the maximum value obtained during the iterations, specifically the maximum of `c` and `maxi` after processing all elements in the list `l`. The final output is calculated as \((2^k \cdot maxi - maxi + sum(l)) \mod 1000000007\).
    #
    #This means that after all iterations of the loop, `maxi` will contain the maximum value of `c` across all iterations, and the final output will be computed using this `maxi`, the given `k`, and the sum of the list `l`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers `a` of length `n` and two positive integers `n` and `k`. For each test case, it calculates a value `maxi` which is the maximum cumulative sum `c` of the list elements under certain conditions (resetting `c` when encountering negative elements whose absolute value is less than or equal to `c`). It then computes the final output as \((2^k \cdot maxi - maxi + sum(a)) \mod 1000000007\) and prints it. The function handles up to \(10^4\) test cases, with \(n\) and \(k\) satisfying \(1 \leq n, k \leq 2 \cdot 10^5\) and the total sum of \(n\) and \(k\) not exceeding \(2 \cdot 10^5\).

