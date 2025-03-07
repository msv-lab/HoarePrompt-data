#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 ⋅ 10^5), and 0 ≤ y ≤ n - x; the sum of x over all test cases does not exceed 2 ⋅ 10^5; the first line of each test case contains three integers n, x, and y; the second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
def func():
    tt = int(input())
    for ii in range(tt):
        n, x, y = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = x + y - 2
        
        tmp = []
        
        for i in range(1, len(a)):
            if a[i] - a[i - 1] == 2:
                ans += 1
            elif (a[i] - a[i - 1]) % 2 == 0:
                tmp.append((a[i] - a[i - 1]) // 2)
        
        if a[0] + n - a[len(a) - 1] == 2:
            ans += 1
        elif (a[0] + n - a[len(a) - 1]) % 2 == 0:
            tmp.append((a[0] + n - a[len(a) - 1]) // 2)
        
        tmp.sort()
        
        for i in tmp:
            if y >= i - 1:
                ans += i
                y -= i - 1
            else:
                break
        
        ans += y
        
        print(min(ans, n - 2))
        
    #State: Output State: tt is the number of test cases; for each test case, `n`, `x`, and `y` are defined based on user input, `a` is a sorted list of integers based on another user input, `ans` is calculated based on the given logic, and the final result is printed as the minimum of `ans` and `n-2`. All other variables retain their initial states.
#Overall this is what the function does:The function processes multiple test cases, each containing integers n, x, and y, followed by x distinct integers from 1 to n. It sorts these integers, calculates a value `ans` based on specific conditions, and adjusts `ans` using a temporary list `tmp`. Finally, it prints the minimum value between `ans` and `n-2` for each test case.

