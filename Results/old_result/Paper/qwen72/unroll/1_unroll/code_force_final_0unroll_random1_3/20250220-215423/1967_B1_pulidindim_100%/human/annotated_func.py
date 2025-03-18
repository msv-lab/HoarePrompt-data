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
        
    #State: The loop will print the value of `ans` for each iteration of the outer loop, where `ans` is calculated based on the input values of `n` and `m` for each iteration. The values of `n` and `m` will be updated from the input for each iteration of the outer loop, and `count` will be reset to 2 for each iteration of the outer loop. The variable `t` will be decremented by 1 for each iteration of the outer loop until it reaches 0.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two positive integers `n` and `m` (where 1 <= n, m <= 2 * 10^6) from the input. It then calculates a value `ans` based on `n` and `m` using a loop, and prints the integer value of `ans` for each test case. The function does not return any value. After the function concludes, the input values `n` and `m` are no longer relevant, and the variable `t` will have been decremented to 0.

