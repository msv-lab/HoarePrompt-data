#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^15; a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9, where a_i represents the durability of the i-th ship. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: T is 0, n is an integer from the input, k is 0, a is a list of integers where all elements have been reduced to zero, l is 0, r is 0, ans is the total count of elements in a that became zero, mi is undefined since the loop has ended, and t is undefined since the loop has ended.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes the number of ships (n), a threshold value (k), and a list of ships' durabilities (a). It then iteratively reduces the durabilities of the ships from both ends towards the center until the threshold value (k) is exhausted or all ships' durabilities become zero. For each ship whose durability becomes zero, it increments a counter (ans). Finally, it prints the total count of ships whose durabilities became zero.

