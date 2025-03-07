#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the array a is a list of n positive integers such that 1 ≤ a_i ≤ n for all i. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: The loop has executed all its iterations, and the final state of the variables is as follows: `total` is 0, `l` and `r` are equal and represent the position where the loop stopped, `a` is a list of integers where each element from index 1 to n-4 is equal to the next one, `le` is the length of list `a`, `st` is the number of consecutive equal elements from the start of the list, `end` is the number of consecutive equal elements from the end of the list, and `ans` is 0 unless `a[0]` equals `a[-1]`, in which case `ans` is `le - (st + end)` but since `st` and `end` are equal and large, `ans` will be 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) positive integers \( a \). For each test case, it calculates the length of the longest subarray where the first and last elements are not part of any consecutive duplicates. Specifically, it counts the number of consecutive identical elements starting from the beginning (`st`) and ending from the end (`end`). If the first and last elements of the list are the same, it adjusts the result accordingly. Finally, it prints the length of the longest subarray that meets the criteria for each test case.

