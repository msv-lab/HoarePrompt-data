#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, representing the size of the array, and a is a list of n integers such that 1 <= a_i <= n, representing the array elements. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case, the loop prints the number of unique elements in the array `a` after removing the longest prefix or suffix of equal elements. If the first and last elements of the array are the same, it prints the number of unique elements after removing both the prefix and suffix of equal elements. The variables `t`, `n`, and `a` remain unchanged for each test case, but the loop iterates through all `t` test cases.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` and a list of `n` integers `a`. For each test case, it calculates and prints the number of elements in `a` that remain after removing the longest prefix or suffix of consecutive equal elements. If the first and last elements of `a` are the same, it removes both the prefix and suffix of equal elements and prints the number of remaining unique elements. The function does not return any value, and the variables `t`, `n`, and `a` are reinitialized for each test case.

