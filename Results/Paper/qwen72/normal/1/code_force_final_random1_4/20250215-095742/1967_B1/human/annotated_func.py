#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: After the loop executes all iterations, `n` and `m` are updated to the values provided by user input for each iteration, `t` remains the same, `i` is `t - 1`, `count` is `m + 1` for the last iteration, `ans` is the final value after all iterations, which is calculated as `n + sum(int((int(n / k) - (k - 1)) / k) + 1 for k in range(2, m + 1))` for each pair of `n` and `m`, `m` must be greater than or equal to the number of iterations the loop executed, `countmins` is `m - 1` for the last iteration, `g` is `int(n / m) - (m - 1)` for the last iteration. If `g` is less than `countmins`, the loop breaks before reaching `count = m + 1` for the last iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads two positive integers `n` and `m` (where 1 <= n, m <= 2 * 10^6). It then calculates a value `ans` starting from `n` and incrementally adds a computed value based on a loop that runs from 2 to `m`. The loop updates `ans` by adding the result of a division operation involving `n` and the current loop index. After processing all test cases, the function prints the final value of `ans` for each test case. The function does not return any value; it only prints the results.

