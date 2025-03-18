#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, k, and x are integers such that 1 <= n <= 2 * 10^5, 1 <= k <= n, and 1 <= x <= n. The array a contains n integers such that 1 <= a_i <= 1000 for each i. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: t
#Overall this is what the function does:The function processes multiple test cases, each involving an array of integers and two integers `k` and `x`. For each test case, it calculates and prints a specific value based on the sum of the array elements, with adjustments made by adding the `k` largest elements and subtracting twice the `x` largest elements, ensuring the result is maximized.

