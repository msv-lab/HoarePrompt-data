#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 4 ≤ n ≤ 10^9, x is an integer where 2 ≤ x ≤ min(n, 2 * 10^5), y is an integer where 0 ≤ y ≤ n - x, and the list of x integers are distinct and within the range [1, n].
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 4 ≤ n ≤ 10^9, `x` is an integer where 2 ≤ x ≤ min(n, 2 * 10^5), `y` is an integer where 0 ≤ y ≤ n - x, `a` is a sorted list of integers with at least 2 elements, `tt` is equal to `t`, `ii` is `t - 1`, `i` is `len(a) - 1`, `tmp` is a list containing the middle points of even differences between consecutive elements in `a` that were less than or equal to `y`, `ans` is the sum of `x + y - 2` plus the number of pairs of consecutive elements in `a` with a difference of 2, plus the sum of the half-differences of pairs of consecutive elements in `a` with an even difference that were less than or equal to `y`, plus the value of `y`.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it takes an integer `n`, two integers `x` and `y`, and a list of `x` distinct integers. It calculates the minimum number of operations needed to ensure that no two adjacent elements in the list have a difference of 2, considering the constraints on `y`. The function prints the result for each test case, which is the minimum of the calculated value and `n - 2`. After processing all test cases, the function terminates.

