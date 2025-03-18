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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the array a is a list of n positive integers such that 1 ≤ a_i ≤ n for all i. After executing the loop, ans is an integer representing the result of the computation based on the conditions given in the loop body, and it is printed for each test case. The sum of all n across all test cases does not exceed 2⋅10^5.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer n and a list of n positive integers a. It then calculates and prints an integer ans based on specific conditions involving the elements of the list a. The value of ans is determined by comparing segments of the list a and adjusting based on certain criteria.

