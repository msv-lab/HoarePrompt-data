#State of the program right berfore the function call: 
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
        
    #State of the program after the  for loop has been executed: T, n, x, s, cnt0, cnt1, balance are positive integers. The final value of n is determined based on the input values and conditions within the loop. If balance is equal to x for any iteration, n is incremented by 1. If the condition (x - balance) % (cnt0 - cnt1) == 0 holds true for any iteration, the loop prints -1. Otherwise, the loop calculates and prints ((x - balance) // (cnt0 - cnt1) + 1).
#Overall this is what the function does:The function `func` reads an input `T`, then iterates `T` times. Within each iteration, it reads two integers `n` and `x`, a string `s`, calculates the difference between the counts of '0' and '1' in `s`, and determines the balance. Depending on the balance compared to `x`, different values are printed. If balance equals `x`, `n` is incremented by 1. If `(x - balance) % (cnt0 - cnt1) == 0`, -1 is printed. Otherwise, the function calculates and prints `((x - balance) // (cnt0 - cnt1) + 1)`. The function does not accept any parameters and does not return any values.

