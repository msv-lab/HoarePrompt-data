#State of the program right berfore the function call: The function should take three parameters: t, a list of pairs (n, k), and a list of lists a. t is an integer (1 ≤ t ≤ 10^4) representing the number of test cases. Each pair (n, k) in the list of pairs consists of integers (1 ≤ n ≤ 2 · 10^5, 1 ≤ k ≤ 10^15) representing the number of ships and the number of attacks by the Kraken, respectively. Each list in a contains n integers (1 ≤ a_i ≤ 10^9) representing the durability of the ships. The length of the list of pairs and the list of lists a should be equal to t. The sum of n for all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has completed all its iterations. `T` is 0, indicating that there are no more test cases to process. For each test case, `l` is equal to `r` or `l` is greater than `r`, and `k` is 0 or less than 2. `ans` is the total number of elements in `a` that have been reduced to 0 during the loop execution, plus 1 if `l` is equal to `r` and `k` is greater than or equal to `a[l]`. The list `a` is modified such that elements that have been reduced to 0 are 0, and the remaining elements are non-zero.
#Overall this is what the function does:The function reads an integer `T` representing the number of test cases. For each test case, it reads two integers `n` and `k`, and a list of `n` integers `a` representing the durability of `n` ships. The function then processes the list `a` by reducing the durability of the ships at the ends of the list, aiming to reduce as many ships to 0 durability as possible using up to `k` attacks. The function prints the number of ships that have been reduced to 0 durability for each test case. After processing all test cases, `T` is 0, and the list `a` for each test case is modified such that the elements that have been reduced to 0 are 0, and the remaining elements are non-zero.

