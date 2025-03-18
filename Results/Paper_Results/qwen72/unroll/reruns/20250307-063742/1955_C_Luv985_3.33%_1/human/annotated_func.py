#State of the program right berfore the function call: The function should take three parameters: t, a list of tuples where each tuple contains n and k, and a list of lists where each sublist contains the durability values a_1, a_2, ..., a_n of the ships. t is an integer such that 1 <= t <= 10^4. Each n is an integer such that 1 <= n <= 2 \cdot 10^5, and each k is an integer such that 1 <= k <= 10^{15}. Each durability value a_i is an integer such that 1 <= a_i <= 10^9. The sum of n for all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: The loop will print the number of ships that have been completely destroyed for each test case, and `T` will be 0 after all iterations.
#Overall this is what the function does:The function reads input from the user and processes multiple test cases. Each test case consists of an integer `n` representing the number of ships, an integer `k` representing the total number of operations available, and a list of integers `a` representing the durability of each ship. The function calculates and prints the number of ships that can be completely destroyed (i.e., their durability reduced to zero or below) using the given operations for each test case. After processing all test cases, the function terminates with `T` being 0.

