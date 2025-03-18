#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 4 <= n <= 10^9, x is an integer such that 2 <= x <= min(n, 2 * 10^5), y is an integer such that 0 <= y <= n - x, and the list of x integers are distinct and within the range 1 to n.
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
        
    #State: The values of `n`, `x`, and `y` will be the last values read from the input during the final iteration of the loop. The list `a` will be the last list of integers read from the input during the final iteration of the loop, sorted in non-decreasing order. The variable `ans` will be the minimum value between the calculated `ans` and `n - 2` for the final iteration of the loop. The list `tmp` will be the last list of integers generated during the final iteration of the loop, sorted in non-decreasing order. The value of `ii` will be `tt - 1`.
#Overall this is what the function does:The function reads a series of test cases from the input. For each test case, it reads three integers `n`, `x`, and `y`, and a list of `x` distinct integers within the range 1 to `n`. It calculates the minimum number of pairs of consecutive integers that can be formed from the list `a` and the additional pairs that can be formed using the integer `y`. The final result is the minimum value between the calculated number of pairs and `n - 2`. The function prints this result for each test case. After the function concludes, the values of `n`, `x`, and `y` will be the last values read from the input during the final iteration, the list `a` will be the last list of integers read and sorted, and the list `tmp` will be the last list of integers generated and sorted.

