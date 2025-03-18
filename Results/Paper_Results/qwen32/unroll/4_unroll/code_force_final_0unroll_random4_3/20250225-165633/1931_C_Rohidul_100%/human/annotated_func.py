#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ n. The sum of n across all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        le = len(a)
        
        l, r = 0, n - 1
        
        st, end = 1, 1
        
        while l < r and a[l] == a[l + 1]:
            l += 1
            st += 1
        
        while r > l and a[r] == a[r - 1]:
            r -= 1
            end += 1
        
        ans = le - max(st, end)
        
        if a[0] == a[-1]:
            ans = max(0, le - (st + end))
        
        print(ans)
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4.
#Overall this is what the function does:The function processes `t` test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the minimum number of elements that need to be removed from the list `a` to make it non-uniform at both ends.

