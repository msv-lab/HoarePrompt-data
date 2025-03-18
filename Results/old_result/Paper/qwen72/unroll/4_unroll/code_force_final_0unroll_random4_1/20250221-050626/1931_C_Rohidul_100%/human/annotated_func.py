#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, representing the size of the array, and a is a list of n integers such that 1 <= a_i <= n, representing the array elements. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case, the loop prints the value of `ans`, which is the length of the array `a` minus the maximum of the lengths of the longest consecutive segments of equal elements at the beginning (`st`) and the end (`end`) of the array. If the first and last elements of the array are the same, `ans` is adjusted to be the length of the array minus the sum of `st` and `end`, ensuring `ans` is non-negative. The variables `t`, `n`, and `a` are not directly modified by the loop, but `l`, `r`, `st`, and `end` are reset for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It calculates and prints a value `ans` for each test case, which represents the length of the array `a` minus the maximum length of the longest consecutive segments of equal elements at the beginning or the end of the array. If the first and last elements of the array are the same, `ans` is adjusted to be the length of the array minus the sum of the lengths of these segments, ensuring that `ans` is non-negative. The function does not return any values, but it prints the result for each test case.

