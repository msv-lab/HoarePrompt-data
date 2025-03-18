#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n, k ≤ 2 · 10^5, representing the length of the array and the number of operations, respectively. The array a consists of n integers a_1, a_2, ..., a_n where -10^9 ≤ a_i ≤ 10^9. The sum of the values of n and k for all test cases does not exceed 2 · 10^5.
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
        
    #State: `i` is `t-1`, `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an input integer, `k` is an input integer, `l` is a list of integers provided by the user, `c` is the sum of all non-negative elements in `l` up to the last positive segment before encountering a negative integer that resets `c` to 0, `maxi` is the maximum value between the previous `maxi` and the current `c`.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `k`, and an array `a` of `n` integers. For each test case, it calculates a specific value based on the array and the number of operations `k`. The final result for each test case is printed, which is the result of the formula `(2

