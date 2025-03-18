#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 ⋅ 10^5, and the sum of the values of n and k for all test cases does not exceed 2 ⋅ 10^5. a is a list of n integers where -10^9 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: The output state is a list of results, each result being the value printed for each test case after executing the given loop. Each result is calculated as \((2^k \times \text{maxi} - \text{maxi} + \text{sum}(l)) \mod 1000000007\), where \(\text{maxi}\) is the maximum contiguous subarray sum under certain conditions, and \(\text{sum}(l)\) is the sum of the list \(l\).
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes two positive integers `n` and `k`, and a list `l` of `n` integers. It calculates the maximum contiguous subarray sum under specific conditions and then computes a value based on this maximum sum, the integer `k`, and the sum of the list `l`. Finally, it prints the result for each test case, which is the value \((2^k \times \text{maxi} - \text{maxi} + \text{sum}(l)) \mod 1000000007\), where \(\text{maxi}\) is the maximum contiguous subarray sum.

