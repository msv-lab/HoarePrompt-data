#State of the program right berfore the function call: t is an integer such that 1 \le t \le 10^4, n and k are integers such that 1 \le n \le 2 \cdot 10^5 and 1 \le k \le 10^{15}, and a is a list of n integers where 1 \le a_i \le 10^9. The sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: `T` is 0, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is the first input integer and must be greater than 1, `k` is 0 or a positive integer that is less than the smallest value in the list `a` after all adjustments, `a` is a list of integers where each integer was originally represented as a string in the list `a`, `l` is the index of the first non-zero element from the left, `r` is the index of the first non-zero element from the right, and `ans` is the total number of elements that have been reduced to 0. If `l` is equal to `r`, `ans` is incremented by 1 if `k` is greater than or equal to `a[l]`.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by three inputs: `n` (the number of elements in a list), `k` (an integer), and `a` (a list of `n` integers). For each test case, it attempts to reduce pairs of elements from the ends of the list `a` by the minimum of the two elements, up to a total reduction of `k`. The function counts how many elements are reduced to zero during this process and prints the count for each test case. After processing all test cases, the function ensures that `T` (the number of test cases) is 0, `k` is 0 or a positive integer less than the smallest non-zero value in `a`, and `ans` is the total number of elements reduced to zero. If `l` (left index) equals `r` (right index) and `k` is greater than or equal to the remaining value at `a[l]`, `ans` is incremented by 1.

