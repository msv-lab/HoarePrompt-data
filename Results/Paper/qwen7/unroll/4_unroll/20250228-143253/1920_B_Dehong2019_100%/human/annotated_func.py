#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, k ≤ n. Additionally, there is a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 1000 for each element in the list. The sum of n across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: After executing the loop for each test case, the value of `ans2` for each test case will be printed. `ans2` represents the maximum possible sum of the array `a` after performing the specified operations.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads values for \( n \), \( k \), \( x \), and a list of \( n \) integers \( a \). It then calculates the maximum possible sum of the list \( a \) after performing specific operations (subtracting and adding elements based on indices). Finally, it prints the maximum sum for each test case.

