#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, n and k are positive integers such that 1 <= n, k <= 2 * 10^5. The array a contains n integers where each element a_i satisfies -10^9 <= a_i <= 10^9. The sum of all n and k across all test cases does not exceed 2 * 10^5.
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
        
    #State: The output state consists of the results of the formula `(2
#Overall this is what the function does:The function processes `t` test cases, each consisting of integers `n` and `k`, and an array `a` of `n` integers. For each test case, it calculates and prints a result based on a specific formula involving the maximum subarray sum, the value of `k`, and the sum of the array elements, modulo 1000000007.

