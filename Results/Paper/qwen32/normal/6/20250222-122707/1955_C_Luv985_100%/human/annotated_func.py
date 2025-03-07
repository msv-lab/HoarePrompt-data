#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^15. a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n across all test cases does not exceed 2 · 10^5.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; T is 0; n and k are the last values read from the input; a is the list of n integers with all elements potentially reduced to 0; l is the final left pointer value; r is the final right pointer value; ans is the final count of elements reduced to 0 plus 1 if l == r and k >= a[l], otherwise unchanged; l is equal to r if the condition l == r was true.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n`, an integer `k`, and a list `a` of `n` integers. It calculates and prints the maximum number of elements in the list `a` that can be reduced to zero by performing operations where pairs of elements are decreased by the same amount, with the total decrease not exceeding `k`.

