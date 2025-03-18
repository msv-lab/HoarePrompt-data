#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 \cdot 10^5, and the sum of the values of n and k for all test cases does not exceed 2 \cdot 10^5. The array a is a list of n integers where each integer a_i satisfies -10^9 ≤ a_i ≤ 10^9.
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
        
        print((2 ** k * maxi - maxi + sum(l)) % 1000000007)
        
    #State: Output State: After the loop executes all the iterations, the variable `maxi` will hold the maximum value between the final value of `c` and the initial value of `maxi` for each test case. The variable `c` will be reset to 0 whenever a negative element in the list `l` is encountered that satisfies the condition `c <= abs(ele)`. The variable `sum(l)` will be the sum of all elements in the list `l`. The variable `2 ** k * maxi - maxi + sum(l)` will be calculated for each test case, and the result will be printed modulo \(10^9 + 7\). The variables `n`, `k`, and `i` will retain their values from the last iteration of the loop.
    #
    #In simpler terms, after all iterations of the loop, `maxi` will contain the highest value of `c` that meets the specified conditions across all test cases. The expression `2 ** k * maxi - maxi + sum(l)` will be computed for each test case, and the results will be printed modulo \(10^9 + 7\).
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \(t\) (number of elements in the array), two positive integers \(n\) and \(k\), and an array \(a\) of \(n\) integers. For each test case, it calculates the maximum value of a running sum \(c\) that is reset under certain conditions involving negative elements in the array. It then computes and prints the result of the expression \(2^k \times \text{maxi} - \text{maxi} + \text{sum}(a)\) modulo \(10^9 + 7\), where \(\text{maxi}\) is the maximum value of \(c\) across the test case.

