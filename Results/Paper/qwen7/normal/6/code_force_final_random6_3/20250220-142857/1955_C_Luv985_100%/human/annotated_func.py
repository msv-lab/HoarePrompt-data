#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ k ≤ 10^15. a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases does not exceed 2·10^5.
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
        
    #State: T is 0, n is an integer greater than 1, k is 0, a is a list of integers where each element has been processed according to the rules inside the loop, l is equal to r and r is 0, ans is an integer greater than or equal to 3, mi is the minimum value between the last two non-zero elements considered in the loop, and t is 0.
#Overall this is what the function does:The function processes a series of test cases. Each test case consists of an integer \( t \) (1 ≤ \( t \) ≤ 10^4), followed by integers \( n \) and \( k \) (1 ≤ \( n \) ≤ 2·10^5, 1 ≤ \( k \) ≤ 10^15), and a list \( a \) of \( n \) integers (1 ≤ \( a_i \) ≤ 10^9). For each test case, it calculates and prints the number of operations needed to reduce all elements in the list \( a \) to zero, where each operation consists of subtracting the same positive integer from two elements of the list. If an element becomes zero during an operation, it is removed from consideration. The function returns nothing explicitly but prints the result for each test case.

