#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n, k, and x are integers for each test case such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ x, k ≤ n, and a is a list of n integers such that 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: t is an input integer, n, k, x are integers for each test case such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ x, k ≤ n, and a is a list of n integers such that 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5. For each test case, the maximum possible value of the modified sum of the list a is printed.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `k`, and `x`, and a list `a` of `n` integers. It then calculates and prints the maximum possible value of a modified sum of the list `a` for each test case. The modified sum is computed by initially summing all elements of `a`, then subtracting twice the value of the first `x` elements, and finally adjusting the sum by adding the value of the first `k` elements and subtracting twice the value of the elements from position `k + x` to the end of the list, if they exist. The function does not return any value; it only prints the results.

