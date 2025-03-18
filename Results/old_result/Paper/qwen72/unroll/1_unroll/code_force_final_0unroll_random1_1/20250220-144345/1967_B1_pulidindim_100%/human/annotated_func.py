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
        
    #State: The value of `t` is decremented by the number of iterations the loop has executed, and `n` and `m` are updated with the last input values read from the user. The variable `ans` is calculated for each iteration and printed, but it does not persist between iterations.
#Overall this is what the function does:The function reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads two positive integers `n` and `m` (1 <= n, m <= 2 * 10^6) from the user. It then calculates a value `ans` based on `n` and `m` and prints this value. The final state of the program after the function concludes is that `t` is reduced by the number of test cases processed, and the last values of `n` and `m` read from the user are retained. The variable `ans` is recalculated and printed for each test case, and it does not persist between test cases.

