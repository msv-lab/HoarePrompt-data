#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^15, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
                if a[l] - t - k // 2 == 0:
                    ans += 1
                break
        
        if l == r:
            ans += k >= a[l]
        
        print(ans)
        
    #State: The loop will print the number of elements in the list `a` that have been reduced to 0 after performing the operations described in the loop for each test case. The variables `T`, `n`, `k`, and `a` will be updated according to the input for each iteration, and the final state of these variables will be the initial state of the next test case or the state after the last test case has been processed.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a long integer `k`, followed by a list `a` of `n` integers. It then performs operations to reduce the elements of `a` to zero by subtracting the minimum of the elements at the current left and right indices, up to a maximum of `k` total subtractions. The function prints the number of elements in `a` that have been reduced to zero after these operations for each test case. The function does not return any value; it only prints the results. After processing all test cases, the function concludes with no further state changes.

