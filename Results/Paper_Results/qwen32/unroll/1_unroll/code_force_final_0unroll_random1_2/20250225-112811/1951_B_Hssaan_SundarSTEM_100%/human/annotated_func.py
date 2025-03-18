#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 2 <= n <= 10^5 and 1 <= k <= n. The list a contains n integers such that 1 <= a_i <= 10^9 and all a_i are pairwise different. The sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n, k = list(map(int, input().split()))
        
        s = list(map(int, input().split()))
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans = 0
        
        h = s[0]
        
        j = -1
        
        for i in s[1:]:
            j += 1
            if h < i:
                break
            else:
                ans += 1
        
        p = j + 1
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans1 = 0
        
        s[p], s[k - 1] = s[k - 1], s[p]
        
        z = 0
        
        for i in s:
            if i == h:
                if s[0] != h:
                    ans1 += 1
                z = 1
            elif i > h:
                break
            elif z == 1:
                ans1 += 1
        
        print(max(ans, ans1))
        
    #State: The output state consists of the printed values for each test case, which are the maximum of `ans` and `ans1` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n` and `k`, and a list `a` of `n` distinct integers. For each test case, it computes and prints the maximum number of elements that can be moved to the beginning of the list while maintaining a non-decreasing order, considering two specific scenarios involving the element at index `k-1`.

