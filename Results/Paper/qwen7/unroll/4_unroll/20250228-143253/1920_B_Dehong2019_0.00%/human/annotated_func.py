#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and x are positive integers satisfying 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n. The array a contains n integers where 1 ≤ a_i ≤ 1000 for all i, and the sum of n across all test cases does not exceed 2⋅10^5.
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
            ans = max(ans1, ans2)
        
        print(ans)
        
    #State: t is an integer representing the number of test cases. For each test case, n, k, and x are integers, a is a list of n integers sorted in non-increasing order. After processing the loop, ans is the maximum value obtained from the operations described in the loop for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers t, n, k, x, and an array a of n integers. For each test case, it sorts the array a in non-increasing order, calculates two values (ans1 and ans2) based on specified operations involving elements of the array, and determines the maximum value between these two. Finally, it prints the maximum value obtained for each test case.

