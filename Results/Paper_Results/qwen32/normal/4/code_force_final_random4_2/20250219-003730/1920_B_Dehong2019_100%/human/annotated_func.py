#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t test cases is described by two lines: the first line contains three integers n, k, and x such that 1 <= n <= 2 * 10^5, 1 <= k <= n, and 1 <= x <= n. The second line contains n integers a_1, a_2, ..., a_n such that 1 <= a_i <= 1000. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The sequence of `ans2` values for each of the `t` test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `k`, `x`, and a list of `n` integers. For each test case, it calculates and prints a specific value `ans2` which is derived by adjusting the sum of the list based on the values of `k` and `x`.

