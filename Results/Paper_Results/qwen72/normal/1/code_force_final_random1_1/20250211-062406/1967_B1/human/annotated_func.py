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
        
    #State: After all iterations, `n` and `m` are the last input integers provided, `t` remains the same as the initial input, `i` is `t - 1`, `count` is `m + 1`, `ans` is the final value calculated by the loop, which is the sum of `n` and the results of the operations performed in each iteration of the loop for each pair of `n` and `m` inputs. For each pair, `countmins` is `m - 1`, and `g` is `int(n / m) - (m - 1)`. If `g` is less than `countmins`, the loop breaks before reaching `count = m + 1`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two positive integers `n` and `m` (where 1 <= n, m <= 2 * 10^6). It then calculates a value `ans` starting from `n` and incrementing it based on a loop that runs from 2 to `m`. The loop modifies `ans` by adding a computed value derived from `n` and the current loop index. After processing all test cases, the function prints the final value of `ans` for each test case. The state after the function concludes includes `t` remaining unchanged, `n` and `m` being the last input values for the final test case, and `ans` being the final calculated value for each test case.

