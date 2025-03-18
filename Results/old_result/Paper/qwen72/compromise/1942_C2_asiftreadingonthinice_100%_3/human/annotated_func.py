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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an input integer, `x` is an input integer, `y` is an input integer, `tt` is an input integer that must be greater than 0, `ii` is `tt - 1`, the list of `x` integers are distinct and within the range [1, n], `a` is a sorted list of integers provided by the user and must have at least `len(a)` elements, `i` is the last element in `tmp` that was processed, `tmp` is a sorted list containing the values of `(a[j] - a[j-1]) // 2` for all `j` in the range 1 to the length of `a` - 1 where `(a[j] - a[j-1]) % 2 == 0` and is not 2, and `tmp` must have at least one element. `ans` is the sum of all elements `i` in `tmp` for which `y` >= `i - 1`, and `y` is updated to `y - (i - 1)` for each such element, plus the value of `y`. `ans` is updated to `min(ans, n - 2)`.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads three integers `n`, `x`, and `y`, and a list of `x` distinct integers `a` within the range [1, n]. It calculates the minimum number of operations needed to ensure that the difference between any two adjacent elements in the sorted list `a` is at least 2, using the value of `y` to perform additional operations if necessary. The function prints the result of this calculation, which is the minimum of `ans` (the calculated number of operations) and `n - 2`. After processing all test cases, the function concludes.

