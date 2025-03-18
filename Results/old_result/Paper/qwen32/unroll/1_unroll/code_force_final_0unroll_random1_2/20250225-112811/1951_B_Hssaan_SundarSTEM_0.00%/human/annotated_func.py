#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of two integers n and k where 2 <= n <= 10^5 and 1 <= k <= n. The second line of each test case contains n integers a_1, a_2, ..., a_n where 1 <= a_i <= 10^9 and all a_i are pairwise different. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: a list of integers where each integer is the result of the maximum of `ans` and `ans1` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of distinct integers and two integers `n` and `k`. For each test case, it calculates and prints the maximum of two values (`ans` and `ans1`) which are derived based on the relative ordering of the elements in the list, particularly in relation to the element at index `k-1`.

