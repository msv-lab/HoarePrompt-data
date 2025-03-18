#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^15; a is a list of n integers such that 1 ≤ a_i ≤ 10^9. It is also guaranteed that the sum of n for all test cases does not exceed 2⋅10^5.
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
        
    #State: The value of `ans` will be the total number of elements in the list `a` that become zero after performing the specified operations for each pair `(n, k)` provided in the input.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes an integer \( n \) (number of elements in the list), an integer \( k \) (a limit value), and a list \( a \) of \( n \) integers. The function performs operations to reduce the values in the list \( a \) by pairs of elements until either the elements are reduced to zero or the limit \( k \) is exhausted. The function counts the number of elements in the list \( a \) that become zero after performing these operations for each test case and prints the count for each test case.

