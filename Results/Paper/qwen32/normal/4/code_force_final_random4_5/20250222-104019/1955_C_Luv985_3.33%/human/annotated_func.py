#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 1 <= n <= 2 * 10^5 and 1 <= k <= 10^15. a is a list of n integers such that 1 <= a_i <= 10^9 for each i. The sum of n across all test cases does not exceed 2 * 10^5.
def func():
    """
        @Time : 2024/8/26 17:59
        @Author : Zhiliang.L
        @Email : 2410103062@mails.edu.cn
        @File : 1955-C.py
    """
    T = int(input())
    while T:
        T -= 1
        
        n, k = input().split()
        
        n = int(n)
        
        k = int(k)
        
        a = input().split()
        
        a = list(map(lambda x: int(x), a))
        
        l = 0
        
        r = n - 1
        
        ans = 0
        
        while l < r and k > 0:
            mi = min(a[l], a[r])
            if mi * 2 <= k:
                a[l] -= mi
                a[r] -= mi
                k -= mi * 2
                if a[l] == 0:
                    ans += 1
                    l += 1
                if a[r] == 0:
                    ans += 1
                    r -= 1
            else:
                t = k % 2
                if mi - t - k // 2 == 0:
                    ans += 1
                break
        
        if l == r:
            ans += k >= a[l]
        
        print(ans)
        
    #State: T is 0, n is the number of elements in the last test case, k is 0 or less, a is the modified array from the last test case, l is the last processed index, r is the last processed index, ans is the total number of fully consumed elements plus 1 if the last element can be fully consumed by the remaining k.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n`, an integer `k`, and a list `a` of `n` integers. It calculates and prints the maximum number of elements from the list that can be fully consumed given the value of `k`, where consuming an element means reducing its value to zero by subtracting from `k`. The function handles each test case independently and outputs the result for each.

