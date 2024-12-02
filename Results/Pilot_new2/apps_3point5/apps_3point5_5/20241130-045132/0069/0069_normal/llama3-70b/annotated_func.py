#State of the program right berfore the function call: $T$ is a positive integer. For each test case, $n$ is a positive integer and $x$ is an integer such that $1 \leq n \leq 10^5$ and $-10^9 \leq x \leq 10^9$. The binary string $s$ has a length of $n$ and consists of 0-s and 1-s.**
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
        
    #State of the program after the  for loop has been executed: The loop will execute T times. After all iterations, balance will be equal to cnt0 - cnt1, n will have a specific value based on the last input, x will be updated to x - balance + cnt0 - cnt1 + 1, and s will contain the last input string entered by the user. If balance is equal to x, n + 1 will be printed. If balance is not equal to x, the value of x will be determined based on the conditions provided in the else part.
#Overall this is what the function does:Functionality: The function `func` reads an integer `T` and then iterates `T` times. For each iteration, it reads integers `n` and `x`, as well as a binary string `s` of length `n`. It calculates the difference in counts of '0's and '1's in `s`, referred to as `balance`. Based on the value of `balance` compared to `x`, the function prints different values: 
- If `balance` equals `x`, it prints `n + 1`.
- If `(x - balance) % (cnt0 - cnt1) == 0`, it prints -1.
- Otherwise, it prints `(x - balance) // (cnt0 - cnt1) + 1`.

The functionality should cover potential edge cases like division by zero errors if `cnt0` is equal to `cnt1`, and any other edge cases that may exist in the input or calculations.

