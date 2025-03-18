#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 4 <= n <= 10^9, x is an integer such that 2 <= x <= min(n, 2 * 10^5), y is an integer such that 0 <= y <= n - x, and the list of x integers are distinct and within the range [1, n].
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
        
    #State: The values of `tt`, `n`, `x`, and `y` are unchanged, and the list `a` is sorted. The variable `ans` is updated to the minimum of the calculated `ans` and `n - 2` for each iteration of the loop.
#Overall this is what the function does:The function `func` reads an integer `tt` indicating the number of test cases. For each test case, it reads three integers `n`, `x`, and `y`, and a list of `x` distinct integers `a` within the range [1, n]. The function calculates a value `ans` based on the differences between consecutive elements in the sorted list `a` and the value of `y`. It then prints the minimum of `ans` and `n - 2` for each test case. The function does not return any value. After the function concludes, the values of `tt`, `n`, `x`, and `y` remain unchanged, and the list `a` is sorted.

