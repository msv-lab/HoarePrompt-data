#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 * 10^5), and y is an integer such that 0 ≤ y ≤ n - x. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen. The sum of x over all test cases does not exceed 2 * 10^5.
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
        
    #State: `ans` is computed for each test case based on the rules described, `ii` is equal to `tt`, and all other variables (`tt`, `t`, `n`, `x`, `y`, `a`, `tmp`) are as per the input for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `x`, and `y`, and a list of `x` distinct integers. For each test case, it calculates and prints a value `ans` which represents a computed result based on the input parameters and list, ensuring that the final output does not exceed `n - 2`.

