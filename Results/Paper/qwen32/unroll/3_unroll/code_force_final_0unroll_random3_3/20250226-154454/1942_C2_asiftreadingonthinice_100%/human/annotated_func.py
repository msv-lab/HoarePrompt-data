#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 · 10^5), and 0 ≤ y ≤ n - x. Additionally, the sum of x over all test cases does not exceed 2 · 10^5. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: a series of printed values, each representing the final `ans` for a test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `x`, and `y`, and a list of `x` distinct integers. For each test case, it calculates and prints a value `ans` that represents the maximum number of vertices Bessie can reach, considering the constraints and the chosen vertices. The final state of the program is a series of printed values, each corresponding to the result of a test case.

