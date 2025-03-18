#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i's are distinct.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i's are distinct; after executing the loop, ans and ans1 are integers representing the maximum value between the two computed values in the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n` and `k`, and a list `a` of `n` distinct integers. For each test case, it swaps the first element of the list with the element at index `k-1`. It then calculates two values, `ans` and `ans1`, based on the list elements and compares them to determine the maximum value. Finally, it prints the maximum value obtained from `ans` and `ans1`.

