#State of the program right berfore the function call: The function should take three parameters: t, a list of pairs (n, k), and a list of lists a. t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each pair (n, k) in the list of pairs represents the number of ships and the number of attacks by the Kraken, with 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^15. Each list in a contains n integers a_1, a_2, ..., a_n, representing the durability of the ships, with 1 ≤ a_i ≤ 10^9. The length of the list of pairs and the list of lists a should be equal to t. The sum of n for all test cases does not exceed 2 · 10^5.
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
        
    #State: `T` is 0, `n` is greater than 1, `k` is 0 or less than the minimum value between `a[l]` and `a[r]` multiplied by 2, `a` is a list of integers, `l` is the index of the first non-zero element from the left or `n` if all elements are zero, `r` is the index of the first non-zero element from the right or `-1` if all elements are zero, and `ans` is the number of elements in `a` that have been reduced to 0. If `l` is equal to `r`, `ans` is incremented by 1 if `k` is greater than or equal to `a[l]`, otherwise `ans` remains unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by a pair of integers (n, k) and a list of integers a. For each test case, it calculates the number of ships that can be completely destroyed by the Kraken, given that the Kraken can perform up to k attacks. The function reads the input for each test case, updates the durability of the ships by simulating the attacks, and prints the number of ships that have been reduced to zero durability. After processing all test cases, the function ensures that the number of test cases `T` is 0, and the final state of the program includes the updated list of ship durabilities `a`, the indices `l` and `r` indicating the positions of the first non-zero elements from the left and right respectively, and the count `ans` of ships that have been destroyed.

