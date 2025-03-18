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
        
    #State: Output State: The output state is a series of integers, each representing the result of the expression \((2^k \times \max(c) - \max(c) + \sum(l)) \mod 1000000007\) for each test case, where \(\max(c)\) is the maximum value of \(c\) calculated during the iteration over the list \(l\), and \(\sum(l)\) is the sum of all elements in the list \(l\). This process is repeated for each test case defined by the input.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers \(n\) and \(k\), and a list \(l\) of \(n\) integers. For each test case, it calculates a value based on the maximum subarray sum (considering negative numbers and their absolute values) and the sum of the list elements. Specifically, it computes \((2^k \times \max(c) - \max(c) + \sum(l)) \mod 1000000007\), where \(\max(c)\) is the maximum value of a running sum \(c\) calculated during the iteration over the list \(l\), and \(\sum(l)\) is the sum of all elements in the list \(l\). The function outputs these computed values for each test case.

