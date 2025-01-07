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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, the values of T, n, x, s, cnt0, cnt1, balance will be the values obtained from the last input operations. The conditions within the loop will determine whether n is incremented, x is incremented, or a specific value is printed based on the calculated balance and x.
#Overall this is what the function does:The function `func` reads an integer `T` from input, then iterates `T` times. Within each iteration, it reads two integers `n` and `x`, a string `s`, calculates the count of '0's and '1's in `s`, computes the balance between the counts, and based on certain conditions prints different values. If the balance equals `x`, it prints `n + 1`, if a certain condition is met, it prints -1, otherwise it calculates and prints a specific value. The function does not accept any parameters and does not return any values.

