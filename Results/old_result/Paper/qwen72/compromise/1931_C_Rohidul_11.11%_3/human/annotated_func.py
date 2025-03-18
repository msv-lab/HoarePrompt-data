#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, representing the size of the array, and a is a list of n integers such that 1 <= a_i <= n, representing the elements of the array. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop has executed `t` times, where `t` is an integer such that 1 <= t <= 10^4. For each test case, `n` is an integer such that 1 <= n <= 2 * 10^5, and `a` is a list of `n` integers such that 1 <= a_i <= n. After processing each test case, the variables `l` and `r` are indices in the list `a` such that `l` is the largest index where `a[l] == a[l + 1]` for all `l < r`, and `r` is the smallest index where `a[r] != a[r - 1]` for all `r > l`. `st` is the number of consecutive elements from the start of the list `a` that are equal, and `end` is the number of consecutive elements from the end of the list `a` that are equal. The variable `ans` is the maximum number of elements in the list `a` that can be removed to make the remaining list have no consecutive equal elements, and it is calculated as follows: If `a[0]` is equal to `a[-1]`, then `ans` is `r - l - 1`. If `a[0]` is not equal to `a[-1]` and both `st` and `end` are 0, then `ans` is `len(a) - 1`. Otherwise, `ans` is `r - l`. The final output is the maximum of 0 and `ans` for each test case.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It calculates the maximum number of elements that can be removed from the list `a` such that the remaining list has no consecutive equal elements. The result for each test case is printed as the maximum of 0 and the calculated number of removable elements. After processing all `t` test cases, the function concludes without returning any value.

