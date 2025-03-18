#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n and k are integers where 1 ≤ n, k ≤ 2 · 10^5, and a is a list of n integers where -10^9 ≤ a_i ≤ 10^9. The sum of the values of n and k for all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates t times, and for each iteration, it processes a list of n integers. After processing, it prints a value calculated from the list and the integer k. The variables t, n, k, and a remain unchanged as they are input values. The loop variables i, c, and maxi are reset for each iteration, and their final values are not retained after the loop completes. The sum of the values of n and k for all test cases does not exceed 2 · 10^5.
#Overall this is what the function does:The function `func` processes `t` test cases, where in each test case, it reads an integer `n` and an integer `k`, followed by a list `l` of `n` integers. For each test case, it calculates the maximum sum of a contiguous subsequence of `l` that is non-negative, and then computes a value using this maximum sum and `k`. The final result for each test case is printed, which is the value `(2

