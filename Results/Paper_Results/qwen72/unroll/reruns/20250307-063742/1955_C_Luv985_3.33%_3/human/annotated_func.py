#State of the program right berfore the function call: The function should take three parameters: t, an integer representing the number of test cases (1 ≤ t ≤ 10^4); a list of tuples, where each tuple contains two integers n and k (1 ≤ n ≤ 2 · 10^5, 1 ≤ k ≤ 10^15) representing the number of ships and the number of attacks by the Kraken, respectively; and a list of lists, where each inner list contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the durability of the ships. The sum of n for all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop will print the number of ships that are destroyed after all the attacks by the Kraken for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of ships and a number of attacks by the Kraken. For each test case, it takes the number of ships `n` and the number of attacks `k`, along with a list of the ships' durability values. The function then simulates the attacks, where the Kraken can either attack two ships at once or a single ship, reducing their durability accordingly. The final output for each test case is the number of ships that are destroyed after all the attacks. The function does not return any value; it prints the result for each test case.

