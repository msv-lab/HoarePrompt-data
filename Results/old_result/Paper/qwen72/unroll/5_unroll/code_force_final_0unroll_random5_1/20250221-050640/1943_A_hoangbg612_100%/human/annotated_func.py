#State of the program right berfore the function call: The function `func` is expected to be called with no arguments, but it should handle multiple test cases. Each test case includes an integer `n` (1 ≤ n ≤ 2 · 10^5) representing the size of the array `a`, and `a` is a list of `n` integers where each integer `a_i` satisfies 0 ≤ a_i < n. The sum of `n` over all test cases does not exceed 2 · 10^5.
def func():
    T = int(input())
    for _ in range(T):
        S = int(input())
        
        N = list(map(int, input().split()))
        
        N.sort()
        
        cur = -1
        
        M = {}
        
        for num in N:
            if num > cur:
                if num > cur + 1:
                    cur += 1
                    break
                cur = num
                M[cur] = 1
            else:
                M[cur] += 1
        
        if sum([M[k] for k in M.keys()]) == S:
            cur += 1
        
        cnt = []
        
        for k in M.keys():
            if M[k] == 1:
                cnt.append(k)
        
        if len(cnt) >= 2:
            cur = cnt[1]
        
        print(cur)
        
    #State: The loop will print the value of `cur` for each test case, which represents the second smallest unique element in the sorted list `N` if there are at least two unique elements. If there are fewer than two unique elements, it will print the largest unique element in the list. The variables `S`, `N`, `M`, and `cnt` will be reset for each iteration of the loop.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `S` and a list `N` of `S` integers. For each test case, it prints the second smallest unique element in the sorted list `N` if there are at least two unique elements. If there are fewer than two unique elements, it prints the largest unique element in the list. The function does not return any value; it only prints the results. The variables `S`, `N`, `M`, and `cnt` are reset for each test case.

