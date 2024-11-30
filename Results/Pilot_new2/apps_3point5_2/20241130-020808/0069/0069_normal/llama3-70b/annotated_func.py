#State of the program right berfore the function call: **
def func():
    T = int(input())
    for _ in range(T):
        n, x = map(int, input().split())
        
        s = input()
        
        cnt0, cnt1 = s.count('0'), s.count('1')
        
        balance = cnt0 - cnt1
        
        if balance == x:
            print(n + 1)
        elif (x - balance) % (cnt0 - cnt1) == 0:
            print(-1)
        else:
            print((x - balance) // (cnt0 - cnt1) + 1)
        
    #State of the program after the  for loop has been executed: `T` is a non-negative integer, `n` is an integer, `x` is an integer, `s` is a string, `cnt0` is the count of '0' in `s`, `cnt1` is the count of '1' in `s`, `balance` is `cnt0 - cnt1`. If `balance == x`, then the value of `n + 1` is printed. If `(x - balance) % (cnt0 - cnt1) == 0`, then -1 is printed. Otherwise, the value of the expression `(x - balance) // (cnt0 - cnt1) + 1` is printed.
#Overall this is what the function does:The function `func` reads an integer `T` from input, then iterates `T` times. For each iteration, it reads integers `n` and `x`, as well as a string `s`. It calculates the count of '0's and '1's in `s`, determines the balance as the difference between the counts, and based on the balance and `x`, it prints either `n + 1`, -1, or a calculated expression. The function does not accept any parameters and only takes input from the user to perform its calculations.

