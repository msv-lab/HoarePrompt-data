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
        
    #State: The values of `n` and `m` are updated for each iteration of the outer loop, and `ans` is calculated based on the updated values of `n` and `m`. After the outer loop completes all `t` iterations, the final values of `n` and `m` are the last inputs provided, and `ans` is printed for each iteration. The value of `t` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` from the input, indicating the number of test cases. For each of the `t` test cases, it reads two positive integers `n` and `m` (where 1 <= n, m <= 2 * 10^6) from the input. It then calculates a value `ans` based on the inputs `n` and `m` and prints the integer value of `ans` for each test case. The values of `n` and `m` are updated for each test case, and the final state of the program after all test cases are processed is that `t` test cases have been completed, with the corresponding `ans` values printed. The value of `t` remains unchanged throughout the function's execution.

