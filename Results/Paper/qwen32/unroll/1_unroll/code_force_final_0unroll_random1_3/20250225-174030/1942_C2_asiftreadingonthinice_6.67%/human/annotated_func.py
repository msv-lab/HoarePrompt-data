#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), y is an integer such that 0 ≤ y ≤ n - x. The sum of x over all test cases does not exceed 2 · 10^5. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
            elif (a[i] - a[i - 1]) % 2 == 0 and y > (a[i] - a[i - 1]) // 2 - 1:
                tmp.append((a[i] - a[i - 1]) // 2)
                ans += (a[i] - a[i - 1]) // 2
                y -= (a[i] - a[i - 1]) // 2 - 1
        
        if a[0] + n - a[len(a) - 1] == 2:
            ans += 1
        elif (a[0] + n - a[len(a) - 1]) % 2 == 0 and y > (a[i] - a[i - 1]) // 2 - 1:
            tmp.append((a[0] + n - a[len(a) - 1]) // 2)
            ans += (a[i] - a[i - 1]) // 2
            y -= (a[i] - a[i - 1]) // 2 - 1
        
        ans += y
        
        print(min(ans, n - 2))
        
    #State: The variables `tt`, `t`, `n`, `x`, and `y` will retain their initial values, and the results for each test case will be printed as per the logic described.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `x`, and `y`, and a list of `x` distinct integers. For each test case, it calculates and prints a value based on the given inputs, representing the result of some computation involving the vertices and the value `y`. The final output for each test case is the minimum of the computed value and `n - 2`.

