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
        
    #State: All test cases have been processed, and `ans` contains the result for each test case based on the conditions specified in the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( t \) indicating the number of subsequent test cases, followed by an integer \( n \) and an array \( a \) of \( n \) positive integers. For each test case, it calculates and prints the length of the array minus the maximum of two segments defined by consecutive equal elements at the beginning and end of the array. If the first and last elements of the array are equal, it adjusts the calculation accordingly.

