#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 10^5, and k is an integer such that 1 <= k <= n. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9, and all a_i's are pairwise distinct. The sum of n over all test cases does not exceed 10^5.
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
        
        p = j
        
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
        
    #State: t is an integer such that 1 <= t <= 10^4. For each test case, the output is the maximum value between `ans` and `ans1`, which represents the longest non-increasing subsequence starting from the first element after the specified swaps. The values of `n`, `k`, and `s` will be those of the last test case processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `k`, and a list `a` of `n` distinct integers. For each test case, it performs specific swaps and calculations to determine the longest non-increasing subsequence starting from the first element after the swaps. It outputs the maximum value between two calculated results for each test case.

