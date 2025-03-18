#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 ⋅ 10^5, and the sum of the values of n and k for all test cases does not exceed 2 ⋅ 10^5. The array a is a list of n integers where -10^9 ≤ a_i ≤ 10^9 for each element a_i.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 ⋅ 10^5, and the sum of the values of n and k for all test cases does not exceed 2 ⋅ 10^5. The array a is a list of n integers where -10^9 ≤ a_i ≤ 10^9 for each element a_i. After executing the loop, the output consists of t lines, each containing one integer which is the result of (2 ** k * maxi - maxi + sum(l)) % 1000000007, where maxi is the maximum subarray sum under certain conditions and sum(l) is the sum of elements in the array l.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( t \) (indicating the number of subsequent test cases), followed by pairs of positive integers \( n \) and \( k \), and an array \( a \) of \( n \) integers. For each test case, it calculates a specific value based on the array \( a \) and the integer \( k \), then prints this value modulo \( 10^9 + 7 \). The calculated value is derived from the maximum subarray sum under certain conditions and the sum of the array elements.

