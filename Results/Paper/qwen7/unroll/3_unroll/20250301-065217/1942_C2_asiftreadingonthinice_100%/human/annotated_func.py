#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x. The sum of x over all test cases does not exceed 2⋅10^5. The first line of each test case contains three integers n, x, and y. The second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: Output State: `tt` is a positive integer such that 1 ≤ `tt` ≤ 10^4. For each `ii` in the range of `tt`, `n`, `x`, and `y` are integers obtained from user input, and `a` is a list of integers also obtained from user input. After processing through the loop, `ans` is calculated based on the given logic and printed as the minimum of `ans` and `n-2`. The final value of `ans` after all iterations is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, x, and y, followed by x distinct integers from 1 to n. It calculates a value `ans` based on specific conditions involving these inputs and the sequence of integers. Finally, it prints the minimum value between `ans` and `n-2` for each test case.

