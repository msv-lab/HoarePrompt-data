#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the array a is a list of n positive integers such that 1 ≤ a_i ≤ n. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the array a is a list of n positive integers such that 1 ≤ a_i ≤ n. The sum of all n across all test cases does not exceed 2⋅10^5. After executing the loop, for each test case, ans is calculated based on the conditions given and printed. The value of ans is determined by the length of the array a, the positions l and r, and the counts st and end.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer \( n \) and a list \( a \) of \( n \) positive integers. It then calculates and prints a value \( ans \) based on specific conditions involving the lengths and values of the list segments. Specifically, it determines \( ans \) as the difference between the length of the list and the maximum of two segment counts, adjusting if the first and last elements of the list are equal.

