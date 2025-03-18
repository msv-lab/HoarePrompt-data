#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 1 <= n, k <= 2 * 10^5. a is a list of n integers where each integer a_i satisfies -10^9 <= a_i <= 10^9. The sum of the values of n and k across all test cases does not exceed 2 * 10^5.
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
        
    #State: t is an integer such that 1 <= t <= 10^4. Each test case has been processed, and the results have been printed. The variables n, k, l, c, and maxi do not retain any specific values as they are local to each iteration.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it calculates and prints a value based on the input integers `n` and `k`, and the list `a` of `n` integers. The calculation involves finding a maximum sum of a subarray under certain conditions, applying a transformation involving `k`, and then taking the result modulo 1,000,000,007.

