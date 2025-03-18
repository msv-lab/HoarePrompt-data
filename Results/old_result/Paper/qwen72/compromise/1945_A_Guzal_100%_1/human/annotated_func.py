#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if b % 3 != 0 and b % 3 + c < 3:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: The values of `a`, `b`, and `c` are updated `n` times based on user input. The variable `k` is reset to 0 at the beginning of each iteration and then calculated based on the conditions provided in the loop. The final state of `a`, `b`, and `c` after the loop will be the values from the last iteration of user input. The value of `k` will be the result of the last calculation performed in the loop.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `n` from the user, which specifies the number of iterations. For each iteration, it reads three non-negative integers `a`, `b`, and `c` from the user, where 0 <= a, b, c <= 10^9. The function calculates a value `k` based on the conditions provided and prints `k` for each iteration. The final state of the program after the function concludes is that `a`, `b`, and `c` will hold the values from the last iteration of user input, and the variable `k` will be the result of the last calculation performed in the loop. The function does not return any value.

