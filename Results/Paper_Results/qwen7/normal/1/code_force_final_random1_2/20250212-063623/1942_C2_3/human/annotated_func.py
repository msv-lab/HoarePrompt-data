#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x; the sum of x over all test cases does not exceed 2⋅10^5; the first line of each test case contains three integers n, x, and y; the second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: After the loop executes all iterations, `ii` will be equal to `tt`, `n` remains unchanged, `x` remains unchanged unless `y` was reduced to zero, `y` is the remaining value after all possible reductions during the loop's iterations, `a` retains its sorted order but may have been altered by the loop's operations, `ans` is updated to be the initial value of `x + y - 2` plus the sum of all valid `y` reductions and the final value of `y`, and `tmp` contains all the integer divisions of the differences by 2 for those pairs where the difference was even and `y` allowed it.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, x, and y, followed by x distinct integers from 1 to n. It calculates a value `ans` based on these inputs, considering specific conditions related to the differences between consecutive integers in the list. The function then prints the minimum value between `ans` and `n - 2`.

