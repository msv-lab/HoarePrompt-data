#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n, k ≤ 2 · 10^5, and a is a list of n integers where -10^9 ≤ a_i ≤ 10^9. The sum of the values of n and k for all test cases does not exceed 2 · 10^5.
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
        
    #State: `c` is 0, `maxi` is the maximum sum of any contiguous subarray in the list `l` for the last test case, `n` is the first integer from the input of the last test case, `k` is the second integer from the input of the last test case, `l` is the list of integers from the input of the last test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers `n` and `k`, and a list `a` of `n` integers. For each test case, it calculates a result based on the maximum sum of any contiguous subarray in the list `a`, adjusted by the value of `k`, and prints the result modulo 1,000,000,007.

