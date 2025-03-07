#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^15. a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9, where a_i represents the durability of the i-th ship. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: T is -1, r is 0, k is 0, l is n - 1, mi is a[l], ans is the total number of times a[l] or a[r] became 0 during the loop's execution plus k >= a[l], a[r] is 0, t is 0, and l is equal to r.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \( t \) (number of test cases), two integers \( n \) and \( k \) (number of ships and a threshold value respectively), and a list of \( n \) positive integers \( a \) (durability of each ship). For each test case, the function determines the number of times the durability of any ship becomes zero when ships are paired and their durabilities are reduced by up to \( k \) units each time, until no more reductions can be made. The function then prints the total count for each test case.

