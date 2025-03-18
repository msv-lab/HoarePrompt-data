#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: All elements in the list `a` are equal, and `ans` is `1` if `a[0]` is equal to `a[-1]`, otherwise `ans` is `0`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates and prints the length of the longest subarray where adjacent elements are equal, adjusting the result if the first and last elements of the list are also equal. If all elements in the list are equal, the result is `1` if the first and last elements are the same, otherwise `0`.

