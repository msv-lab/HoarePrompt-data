#State of the program right berfore the function call: t is a positive integer, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of all n across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: t is a positive integer, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. After executing the loop, the variable ans contains the value calculated based on the conditions inside the loop for each test case, and is printed for each test case. The variables l, r, st, and end are reset to their initial values at the start of each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers \( a \). For each test case, it calculates and prints a value based on specific conditions involving the lengths of consecutive identical elements at the beginning and end of the list \( a \). Specifically, it determines the maximum length of consecutive identical elements at the start and end of the list, subtracts this maximum from the total length of the list, and adjusts the result if the first and last elements of the list are identical.

