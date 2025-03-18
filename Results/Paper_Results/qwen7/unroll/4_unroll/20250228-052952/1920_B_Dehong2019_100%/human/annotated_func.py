#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n; and a is a list of n integers such that 1 ≤ a_i ≤ 1000. Additionally, the sum of n over all test cases does not exceed 2⋅10^5.
def func():
    """
    Created on Fri Sep  6 21:42:15 2024
     
    @author: dehon
    """
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        
        a = sorted(list(map(int, input().split())), reverse=True)
        
        ans1 = sum(a)
        
        for i in range(x):
            ans1 -= a[i] * 2
        
        ans2 = ans1
        
        for i in range(k):
            ans1 += a[i]
            if i + x < n:
                ans1 -= a[i + x] * 2
            ans2 = max(ans1, ans2)
        
        print(ans2)
        
    #State: Output State: t is an input integer, and for each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n; and a is a list of n integers such that 1 ≤ a_i ≤ 1000. After executing the loop, ans2 contains the maximum value of ans1 after performing the specified operations for each test case. The sum of n over all test cases does not exceed 2⋅10^5.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers \( t \), \( n \), \( k \), and \( x \), along with a list \( a \) of \( n \) integers. It then sorts the list \( a \) in descending order, calculates two values \( ans1 \) and \( ans2 \) based on specific operations involving elements of \( a \) and the given integers \( x \) and \( k \). Finally, it prints the maximum value of \( ans1 \) after performing these operations for each test case.

