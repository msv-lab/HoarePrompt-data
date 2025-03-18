#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 1 <= a_i <= n. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        l, r = 0, n - 1
        
        st, end = 0, 0
        
        while l < r and a[l] == a[l + 1]:
            l += 1
            st += 1
        
        while r > l and a[r] == a[r - 1]:
            r -= 1
            end += 1
        
        if a[0] == a[-1]:
            ans = r - l - 1
        elif st == 0 and end == 0 and a[0] != a[-1]:
            ans = len(a) - 1
        else:
            ans = r - l
        
        print(max(0, ans))
        
    #State: The loop processes each test case, and for each test case, it prints the maximum of 0 and the calculated value of `ans`. The variables `t`, `n`, and `a` are reset for each test case, and the final state of these variables is undefined after the loop completes. The variables `l`, `r`, `st`, `end`, and `ans` are only relevant within each test case and are recalculated for each iteration.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates and prints the maximum of 0 and a value `ans`, which represents the length of the longest subarray of `a` that does not contain consecutive duplicate elements, adjusted based on the presence of duplicates at the start and end of the list. The function does not return any value; it only prints the result for each test case. After processing all test cases, the state of the variables `t`, `n`, and `a` is undefined.

