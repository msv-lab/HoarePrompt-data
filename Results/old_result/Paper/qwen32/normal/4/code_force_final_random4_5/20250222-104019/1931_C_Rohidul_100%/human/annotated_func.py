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
        
    #State: The output of the last test case, which includes the final values of `l`, `r`, `st`, `end`, and `ans` after processing the last list `a` with length `n`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n` and a list `a` of `n` integers. It calculates and prints a value for each test case based on the list `a`. The value printed represents the minimum number of elements to remove from the list so that the remaining list does not have the same starting and ending elements that are also the same as the longest contiguous segments at the start or end of the list.

