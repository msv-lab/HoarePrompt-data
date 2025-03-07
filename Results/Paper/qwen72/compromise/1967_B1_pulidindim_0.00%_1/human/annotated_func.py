#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = count - 1
            g = n / count
            if g < countmins:
                break
            g -= countmins
            ans += g / count + 1
            count += 1
        
        print(int(ans))
        
    #State: After all iterations, `n` and `m` are updated to the values provided by the user for each iteration, `t` is greater than or equal to the number of iterations, `i` is `t - 1`, `count` is `m + 1` for each iteration, `ans` is the sum of `n` and the series of values added in each iteration where `g` is `n / count - (count - 1)`, `countmins` is `m - 1` for each iteration, and `g` is the final value of `n / m - (m - 1)` for each iteration. If `g` is less than `countmins` for any iteration, the loop breaks for that iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads two positive integers `n` and `m` (1 <= n, m <= 2 * 10^6). It then performs a series of calculations to compute a value `ans` based on `n` and `m`. The final value of `ans` is printed for each test case. After all iterations, `t` is greater than or equal to the number of test cases, and `n` and `m` are updated to the values provided by the user for each test case. The function does not return any value.

