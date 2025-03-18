#State of the program right berfore the function call: t is a positive integer where 1 ≤ t ≤ 10^4; n, x, and y are integers where 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 · 10^5), and 0 ≤ y ≤ n - x; the second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: `t` is a positive integer where 1 ≤ t ≤ 10^4, `n` is an input integer where 4 ≤ n ≤ 10^9, `x` is an input integer where 2 ≤ x ≤ min(n, 2 · 10^5), `y` is an input integer, `tt` is equal to the initial value of `tt`, `ii` is `tt - 1`, `i` is `len(a) - 1`, `a` is a sorted list of integers in ascending order, `tmp` is a list of integers, and `ans` is the final computed value based on the loop's operations for all iterations.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers `n`, `x`, and `y`, followed by a list of `x` distinct integers. For each test case, it calculates a value `ans` based on the differences between the sorted list of integers and the values of `x` and `y`. The function then prints the minimum of `ans` and `n - 2`. After processing all test cases, the function terminates, leaving the input variables `t`, `n`, `x`, `y`, and the list of integers in their final states as described in the annotations.

