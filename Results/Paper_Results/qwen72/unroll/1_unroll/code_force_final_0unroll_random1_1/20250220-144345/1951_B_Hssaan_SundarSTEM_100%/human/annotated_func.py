#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 2 ≤ n ≤ 10^5, k is an integer such that 1 ≤ k ≤ n, and a is a list of n integers where 1 ≤ a_i ≤ 10^9 and all a_i are distinct. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it prints the maximum number of elements in the list `s` that can be made non-decreasing by swapping the first element with the k-th element or by swapping the first element with the k-th element and then swapping the element at position `p` with the k-th element. The values of `t`, `n`, `k`, and `a` remain unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and an integer `k`, followed by a list `s` of `n` distinct integers. The function then determines and prints the maximum number of elements in the list `s` that can be made non-decreasing by performing one or two specific swaps: either swapping the first element with the `k`-th element, or swapping the first element with the `k`-th element and then swapping the element at position `p` (determined during the process) with the `k`-th element. The values of `t`, `n`, `k`, and the list `s` remain unchanged after the function concludes.

