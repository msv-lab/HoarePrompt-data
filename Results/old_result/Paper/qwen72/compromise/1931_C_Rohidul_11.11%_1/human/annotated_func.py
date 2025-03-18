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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an input integer greater than 1 for each test case, `a` is a list of integers provided by the user input for each test case, `l` and `r` are indices such that `l` is the smallest index where `a[l]` is not equal to `a[l + 1]` and `r` is the largest index where `a[r]` is not equal to `a[r - 1]`, `st` is the number of consecutive elements from the beginning of the list `a` that are equal to `a[0]`, `end` is the number of consecutive elements from the end of the list `a` that are equal to `a[-1]`. For each test case, if `a[0]` is equal to `a[-1]`, then `ans` is `r - l - 1`. Otherwise, if `st` is 0 and `end` is 0, then `ans` is `len(a) - 1`. If either `st` is not 0 or `end` is not 0, then `ans` is `r - l`.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It calculates the number of elements in the list `a` that are not part of the longest prefix or suffix of consecutive equal elements. The result for each test case is printed, and it is the maximum of 0 and the calculated value.

