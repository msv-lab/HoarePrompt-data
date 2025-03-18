#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, n is an integer such that 1 <= n <= 500.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum, r = 0, 0
        
        for i in range(1, n + 1):
            if n * (n + 1) // 2 > i * n:
                r = i
                sum += n * (n + 1) // 2
            else:
                sum += i * n
        
        print(sum, n + r)
        
        for j in range(1, n + r + 1):
            if j <= n:
                print(1, j, end=' ')
                print(*range(1, n + 1))
            else:
                print(2, j % n, end=' ')
                print(*range(1, n + 1))
        
    #State: The loop will execute `t` times, and for each iteration, it will read an integer `n` from the user. After each iteration, the variables `sum` and `r` will be reset to 0, and the loop will print the final values of `sum` and `n + r`. Additionally, it will print a series of lines based on the value of `n + r`. The state of `t` will remain unchanged, and the loop will continue to execute until all `t` test cases have been processed.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, where `1 <= t <= 500`. It then processes `t` test cases. For each test case, it reads an integer `n` from the user, where `1 <= n <= 500`. After processing each test case, the function prints the sum of certain values and the value of `n + r`, where `r` is determined based on the relationship between `n` and `i`. Additionally, it prints a series of lines, each containing a sequence of numbers based on the value of `n + r`. The function does not return any value; it only performs these print operations. The state of `t` remains unchanged throughout the function execution.

